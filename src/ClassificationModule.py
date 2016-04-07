#-*- coding: utf-8 -*-
import os
import Constants
import codecs
from CleaningTextMaster import CleaningText
from BookModule import Book
from AuthorModule import Author
import Utils
import matplotlib.pyplot as plt
from Statistics import Statistics

class Classification(object):
    def __init__(self, cleaning):
        self.cleaning = cleaning
        self.books = list()
        self.authors_name = list()
        
    def get_books(self):
        return self.books
    
    def get_authors(self):
        return self.authors_name
    
    def get_distance(self):
        for book in self.books:
            for author in self.authors_name:
                if (book.get_author() == author.get_name()):
                    book.calculate_proximity(author)
                else: 
                    book.calculate_similarity(author)
    
    def get_stationary_len(self):
        for book in self.books:
            book.calculate_stationary_length()
            book.print_stat_len(Constants.stat_lenght_filepath)
        
    def load_dirty_books(self, name_dirty_dir, name_clean_dir):
        print "start loading dirty library from ", name_dirty_dir   
        for folder in os.listdir(name_dirty_dir):
            opendir = os.path.join(name_dirty_dir,folder)
            author_books = list()
            clean_dir_name = os.path.join(name_clean_dir,folder)
            os.mkdir(clean_dir_name)
            for fname in os.listdir(opendir):
                print "load: ", fname
                path = os.path.join(opendir,fname)
                ##Problem with encoding sometimes
                if (Constants.language == 'ru'):
                    text = open(path)
                    txt = text.read().decode('cp1251')
                else:
                    text = codecs.open(path,encoding="utf-8")
                    txt = text.read()                
                clean_text = CleaningText(text=txt,filename=fname)           
                clean_text.put_in_file(clean_dir_name)
                book = Book(filename=fname, text=clean_text.get_text())
                self.books.append(book)
                #book.print_dict_in_file(Constants.ngrams_path)
                book.print_book_description_in_file(Constants.classif_info_filepath)
                author_books.append(book) 
            author = Author(name=folder, books=author_books)
            self.authors_name.append(author)
        print "loaded"
        
    def load_claen_books(self,name_clean_dir):
        print "start loading clean library from ", name_clean_dir   
        for folder in os.listdir(name_clean_dir):
            opendir = os.path.join(name_clean_dir,folder)
            author_books = list()
            for fname in os.listdir(opendir):
                path = os.path.join(opendir,fname)
                text = codecs.open(path, 'r',"utf-8")
                txt = text.read()
                book = Book(filename=fname, text=txt)
                self.books.append(book)
                #book.print_book_description_in_file(Constants.classif_info_filepath)
                author_books.append(book) 
            author = Author(name=folder, books=author_books)
            self.authors_name.append(author)
        print "loaded"
    
                    
    def start_classification(self):
        static_file = open(Constants.classif_info_filepath,'a')
        static_file.write(Utils.get_safe_time_string()+" CLASSFICATION "+'\n')
        if self.cleaning:
            self.load_dirty_books(Constants.classif_dirty_book_path, Constants.classif_clean_book_path)
        else: 
            self.load_claen_books(Constants.classif_clean_book_path)
        static_file.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        static_file.close()
        self.get_distance()
        self.get_classification_results(Constants.classif_info_filepath)
        #self.print_detail_classif_results(Constants.classif_info_filepath)
        #self.drow_stat_len()
    
            
    def get_classification_results(self, file_name):
        result_file = open(file_name,'a')
        print "Results will be in ", file_name
        result_file.write(Utils.get_safe_time_string()+" CLASSIFICATION RESULTS:"+'\n' )
        right = 0
        error = 0
        for book in self.books:
            near_author = book.get_near_author()
            result_file.write(book.get_author()+', '+ near_author)
            if (near_author == book.get_author()):
                right +=1
                result_file.write("\n")
            else:
                error +=1
                result_file.write(" error\n")
        result = float(right) / (right + error)* 100
        result_file.write('right: '+ str(right) + 'wrong: ' + str(error) + 'percent: ' + str(result)+ '%')
        result_file.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        result_file.close()
        
    def collect_statistics(self):
        self.load_claen_books(Constants.classif_clean_book_path)
        self.get_distance()
        stat = Statistics(books=self.books, authors=self.authors_name)
        stat.collcet_statistic()
        
    def print_detail_classif_results(self,file_name):
        print "Results will be in ", file_name
        result_file = open(file_name,'a')
        result_file.write(Utils.get_safe_time_string()+" CLASSIFICATION RESULTS:"+'\n' )
        for book in self.books:
            result_file.write('____________________________\n')    
            result_file.write('AuthorModule: {0:15} | Book: {1:30}'.format(book.get_author(),book.get_name())+'\n')
            dist = book.get_distance()
            for a, d in dist.items():
                result_file.write('{0:15} | {1}'.format(a,d)+'\n')      
        result_file.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        result_file.close()
    
    def drow_stat_len(self):
        self.get_stationary_len()
        for author in self.authors_name:
            #plt.axis([0, 1.0, 0, 800000])          
            plt.ylabel(u'Длина текста')
            plt.xlabel(u"Уровень стационарности")
            plt.title(u'Зависимость длины стационарности от уровня стационарности для произведений '+ author.get_name())
            plt.grid(True)
            #plt.legend()
            for book in author.get_books():
                stat_len, stat_level = book.get_stationary_len()
                plt.plot(stat_level,stat_len, label=book.get_name())
            plt.xticks([0, 0.01, 0.02, 0.03, 0.04, 0.05,0.06, 0.07, 0.08, 0.09, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4])
            plt.xlim(xmax=0.4)
            plt.legend()               
            plt.show()
        
    

                
            
        
    
        