#-*- coding: utf-8 -*-
import os
from CleaningTextMaster import CleaningText
from BookModule import Book
import Constants
import codecs

class Library():
    def __init__(self, cleaning = True, ngr = True):
        self.cleaning = cleaning
        self.books = list()
        self.authors_name = list()
                    
    def get_books(self):
        return self.books
    
    def get_authors(self):
        return self.authors_name
             
    def load_dirty_books(self, name_dirty_dir, name_clean_dir):
        print "start loading dirty library from ", name_dirty_dir   
        for fname in os.listdir(name_dirty_dir):
            print "load: ", fname
            path = os.path.join(name_dirty_dir,fname)
            ##Problem with encoding sometimes
            if (Constants.language == 'ru'):
                text = open(path)
                txt = text.read().decode('cp1251')
            else:
                text = codecs.open(path,encoding="utf-8")
                txt = text.read()                
            clean_text = CleaningText(text=txt,filename=fname)           
            clean_text.put_in_file(name_clean_dir)
            book = Book(filename=fname, text=clean_text.get_text())
            if not (book.get_author() in self.authors_name):
                self.authors_name.append(book.get_author())         
            self.books.append(book)
        print "loaded"
        
        
    def load_clustring_clean_books(self,dir_name):
        print "load clean books for clustering from ", dir_name
        for fname in os.listdir(dir_name):
            print "load: ", fname
            path = os.path.join(dir_name,fname)
            text = codecs.open(path, 'r',"utf-8")
            txt = text.read()             
            book = Book(filename=fname, text = txt)
            if not (book.get_author() in self.authors_name):
                self.authors_name.append(book.get_author())         
            self.books.append(book)
        print "loaded"
            

        
        
            
        
        
            
            
    
        
           
            
            
            
            
                
                
            
            

        
       
            
        
        

        