#-*- coding: utf-8 -*-
import Constants
import Utils

class Classification(object):
    def __init__(self, books, authors, language="ru"):
        self.books = books
        self.authors = authors
        self.language = language
        
    def get_books(self):
        return self.books
    
    def get_authors(self):
        return self.authors
    
    def get_distance(self):
        for book in self.books:
            for author in self.authors:
                if (book.get_author() == author.get_name()):
                    book.calculate_proximity(author)
                else: 
                    book.calculate_similarity(author)                           
                     
    def start_classification(self):
        static_file = open(Constants.classif_info_filepath,'a')
        static_file.write(Utils.get_safe_time_string()+" CLASSFICATION "+'\n')
        static_file.close()
        self.get_distance()
        self.get_classification_results(Constants.classif_info_filepath)
        #self.print_detail_classif_results(Constants.results_filepath)
    
            
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
        print 'right: '+ str(right) + 'wrong: ' + str(error) + 'percent: ' + str(result)+ '%'+'\n'
        result_file.write(' right: {0} wrong:{1} error:{2} percent:{3} %'.format(str(right),str(error),str(result)))
        result_file.close()      
                
    def print_detail_classif_results(self,file_name):
        print "Results will be in ", file_name
        result_file = open(file_name,'a')
        result_file.write(Utils.get_safe_time_string()+" CLASSIFICATION RESULTS:"+'\n' )
        for book in self.books:
            result_file.write('____________________________\n')    
            result_file.write('AuthorModule: {0:15} | Book: {1:30}| Lenght: {2}'.format(book.get_author(),book.get_name(), book.get_length())+'\n')
            dist = book.get_distance()
            for a, d in dist.items():
                result_file.write('{0:15} | {1}'.format(a,d)+'\n')      
        result_file.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        result_file.close()
    

            
                
                    
                    
        
        
    

                
            
        
    
        