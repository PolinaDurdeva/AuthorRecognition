#-*- coding: utf-8 -*-
import os
from CleaningTextMaster import CleaningText
from BookModule import Book
import Constants
import codecs
from AuthorModule import Author

class Library():
    def __init__(self, cleaning = True):
        self.cleaning = cleaning
        self.books = list()
        self.authors = list()
        
                    
    def get_books(self):
        return self.books
    
    def get_authors(self):
        return self.authors
    
    def get_authors_name(self):
        authors_name = list()
        for author in self.authors:
            authors_name.append(author.get_name())
        return authors_name
             
    def load_library(self,language):
        if (self.cleaning):
            self.load_dirty_library(language)
        else:
            self.load_clean_library(language)    
    
    def load_dirty_library(self, language="ru"):
        print "start loading dirty library"
        library_categories = os.listdir(Constants.dirty_library)
        target_folder = os.path.join(Constants.dirty_library,language)
        if not (language in library_categories):
            print "Language is not"
        clean_folder = os.path.join(Constants.clean_library,language)     
        if language in os.listdir(Constants.clean_library):
            print clean_folder
            os.remove(clean_folder)
            os.mkdir(clean_folder)
        else:
            os.mkdir(clean_folder)    
        for folder in os.listdir(target_folder):
            opendir = os.path.join(target_folder,folder)
            author_books = list()            
            clean_dir_name = os.path.join(clean_folder,folder)
            os.mkdir(clean_dir_name)
            for fname in os.listdir(opendir):
                print "load: ", fname
                path = os.path.join(opendir,fname)
                ##Problem with encoding sometimes
                if (language == 'ru'):
                    text = open(path)
                    txt = text.read().decode('cp1251')
                else:
                    text = codecs.open(path,encoding="utf-8")
                    txt = text.read()  
                clean_text = CleaningText(text=txt,filename=fname,lang=language)           
                clean_text.put_in_file(clean_dir_name)
                book = Book(author=folder, name=fname, text=clean_text.get_text())
                self.books.append(book)
                #book.print_dict_in_file(Constants.ngrams_path)
                book.print_book_description_in_file(Constants.classif_info_filepath)
                author_books.append(book) 
            author = Author(name=folder, books=author_books)
            self.authors.append(author)
        print "loaded"  
        
    
    def load_clean_library(self, language="ru"):
        print "start loading clean library"
        clean_folder = os.path.join(Constants.clean_library,language)       
        for folder in os.listdir(clean_folder):
            opendir = os.path.join(clean_folder,folder)           
            author_books = list()
            f = 0
            for fname in os.listdir(opendir):               
                if (f > 5):
                    break                    
                f += 1
                path = os.path.join(opendir,fname)
                text = codecs.open(path, 'r',"utf-8")
                txt = text.read()
                #if (len(txt) > 2000):
                book = Book(author=folder,name=fname, text=txt)
                self.books.append(book)
                author_books.append(book)
                #book.print_dict_in_file(Constants.ngrams_path)
                #book.print_book_description_in_file(Constants.classif_info_filepath)
            author = Author(name=folder, books=author_books)
            self.authors.append(author)            
        print "loaded"
        
        
              

        
        
            
        
        
            
            
    
        
           
            
            
            
            
                
                
            
            

        
       
            
        
        

        