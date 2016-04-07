import os
from BookModule import Book
import numpy as np
import Constants
import numpy as np


class Author(object):

    def __init__(self, name, books):
        print  "author is loaded"
        self.name = name
        self.books = books
        self.count_book = len(self.books)
        self.sum_gramm = 0
        self.avg_pfr = list()
        ###
        self.set_avg_pfr()
   
    def get_name(self):
        return self.name
    
    def get_books(self):
        return self.books
    
    def get_sum_gramm(self):
        return self.sum_gramm
        
    def get_avg_pfr(self):
        return np.array(self.avg_pfr)
    
    def set_avg_pfr(self):
        sum_gr = 0   
        lenght = len(Constants.set_pfr)
        sum_pfr = np.zeros(lenght)
        for book in self.books:
            c_ng = book.get_length()/book.get_N()
            tmp = book.get_pfr()* c_ng
            sum_pfr += tmp          
            sum_gr+= c_ng
        self.avg_pfr = sum_pfr/sum_gr
        self.sum_gramm = sum_gr
    
   # def get_avg_book(self):
        
                   
            
            
            
            
               
        
        
        
        
        
        