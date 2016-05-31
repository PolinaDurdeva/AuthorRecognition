import numpy as np
import Constants
import sys

class Author(object):

    def __init__(self, name, books):
        self.name = name
        self.books = books
        self.count_book = len(self.books)
        self.count_ngramm = 0
        self.author_pfr = list()
        ###
        self.set_author_pfr()
        print  "author is loaded"
   
    def get_name(self):
        return self.name
    
    def get_books(self):
        return self.books
    
    def get_sum_gramm(self):
        return self.count_ngramm
        
    def get_author_pfr(self):
        return np.array(self.author_pfr)
    
    def get_book_min_len(self):
        min_len = sys.maxint
        for book in self.books:
            if (book.get_length() < min_len):
                min_book = book
                min_len = book.get_length()
        return min_book 
    
    def get_book_max_len(self):
        max_len = 0
        for book in self.books:
            if (book.get_length() > max_len):
                max_book = book
                max_len = book.get_length()
        return max_book
               
    
    def set_author_pfr(self):
        count_ngramm = 0   
        lenght = len(Constants.set_pfr)
        sum_pfr = np.zeros(lenght)
        for book in self.books:
            c_ng = book.get_length()
            sum_pfr += book.get_pfr() * c_ng          
            count_ngramm += c_ng
        self.author_pfr = sum_pfr/count_ngramm
        self.count_ngramm = count_ngramm
    
        
                   
            
            
            
            
               
        
        
        
        
        
        