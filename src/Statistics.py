#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from AuthorModule import Author
import numpy as np
from math import sqrt
import sys
import Constants

class Statistics():

    def __init__(self, books = None, authors = None):
        self.books = books
        self.authors = authors
        self.step = 0.02
        ##
        self.count_book = len(self.books)
        self.count_author = len(self.authors)
        ##
        self.distance_s = list()
        self.distance_o = list()
        self.dist_between_books = list()
       
    def get_distance(self):
        for book in self.books:
            for author in self.authors:
                if (book.get_author() == author.get_name()):
                    book.calculate_proximity(author)
                else: 
                    book.calculate_similarity(author)   
                    
    def avg_distance_to_other_author(self):
        print "Среднее расстояние от книги до чужого эталона"
        for author in self.authors:
            avg_dist = 0
            v = 0
            for book in author.get_books():
                avg_dist += sum(book.get_distance())
                v += len(book.get_distance())
            print author.get_name(), ";", float(avg_dist) / v
            
        
    def distance_between_pfr(self,pfr,other_pfr):
        dist = sum(np.absolute(np.array(pfr) - np.array(other_pfr)))
        return dist 
         
    ## Расстояние от книги до чужого авторского представителя 
    def collect_distance_o(self):
        for book in self.books:
            for author in self.authors:
                if (book.get_author() != author):
                    self.distance_o.append(book.get_distance()[book.get_author()])   
        
    ## Расстояние между книгами                    
    def collect_dist_between_books(self):
        for book in self.books:
            for other in self.books:
                if (book.get_name() != other.get_name()):
                    self.dist_between_books.append(self.distance_between_pfr(book.get_pfr(), other.get_pfr()))
         
                    
    ## Расстояние от книги до своего авторского представителя            
    def collect_distance_s(self):
        for book in self.books:
            self.distance_s.append(book.get_distance()[book.get_author()])          
        
    def pdf(self,arr):
        return np.histogram(arr, bins=np.arange(0,1.0 + self.step, self.step))
    
    def cdf(self, histogram):
        distribution = list()
        sum = 0
        for i in histogram:
            sum+=i
            distribution.append(sum)         
        return distribution

    def pmax(self,arr):
        i = 0
        p = 0
        while (arr[i] == 0):
            p+=self.step
            i+=1
        return p
    
    def pmin(self,arr):
        i = 0
        p = 0
        lenght = len(arr)
        while (i < lenght) and (arr[i] < 0.99):
            p+=self.step
            i+=1
        return p
    
    def h1_error(self,arr, pmin):
        index = int( pmin / self.step)
        return arr[index-1]
    
    def h2_error(self,arr,pmax):
        index = int( pmax / self.step)
        return 1 - arr[index-1]
    
    def p_separation(self,arr1, arr2):
        max=0
        ind = -1
        for i in range(len(arr1)):
            sum = arr1[i] + arr2[i]
            if (sum > max):
                max = sum
                ind = i
        return ind*self.step
    
    def collect_statistics(self):
        self.get_distance()
        self.avg_distance_to_other_author()
        self.collect_distance_s()
        self.collect_distance_o()
        pdf_s, xs = self.pdf(self.distance_s)
        print pdf_s
        pdf_o, xo = self.pdf(self.distance_o)
        pdf, x = self.pdf(self.dist_between_books)
        cdf_o = self.cdf(np.array(pdf_o)/float(len(self.distance_o)))
        cdf_s = self.cdf(np.array(pdf_s)/float(len(self.distance_s)))
        pmin = self.pmin(cdf_s)
        pmax = self.pmax(cdf_o)
        h1_error = self.h1_error(cdf_o, pmin)
        h2_error = self.h2_error(cdf_s, pmax)
        p_sep = self.p_separation(cdf_o, cdf_s)
        mean_s = np.mean(self.distance_s)
        mean_o = np.mean(self.distance_o)
        std_s = np.std(self.distance_s)
        std_o = np.std(self.distance_o)
        #output = open(output_file, 'a')
        #output.write(str)
        #print cdf_o
        #print cdf_s
        print 'pmin= ', pmin, ' pmax = ', pmax, ' p sep = ', p_sep
        print 'h1 error = ', h1_error, ' h2_error = ', h2_error
        print 'mean other = ', mean_o, " mean self = ", mean_s  
        print 'std other = ', std_o, " std self = ", std_s 
        self.get_avg_len_of_books()
    
    def get_avg_len_of_books(self):
        arr_len = list()
        for book in self.books:
            arr_len.append(book.get_length())
        print "avg legth of books", (np.mean(np.array(arr_len)))
        print "std length of books", ((np.std(np.array(arr_len))))
                  
            
    def get_maxmin_len_of_books(self): 
        for author in self.authors:
            print author.get_name()
            print "book max length", author.get_book_max_len().get_length()
            print  "book min length ", author.get_book_min_len().get_length()

                    
    def grafic_show(self, arr, bins, title):
        plt.ylabel(u'Вероятность')
        plt.xlabel(u"Расстояние")
        plt.title(title)
        plt.grid(True)
        plt.hist(arr, bins = bins, normed=True)  # plt.hist passes it's arguments to np.histogram
        plt.show()

    def get_stationary_len(self):       
        for book in self.books:
            book.calculate_stationary_length()
            book.print_stationary_length_in_file(Constants.stat_lenght_filepath)  

    def drow_stat_len(self):
        for author in self.authors:
            #plt.axis([0, 1.0, 0, 800000])          
            plt.ylabel(u'Длина текста')
            plt.xlabel(u"Уровень стационарности")
            plt.title(u'Зависимость длины стационарности от уровня стационарности для произведений '+ author.get_name())
            plt.grid(True)
            #plt.legend()
            for book in author.get_books():
                stat_len, stat_level = book.get_stationary_len()
                plt.plot(stat_level,stat_len, label=book.get_name())
            plt.xticks([0,0.02,0.04,0.06,0.08, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4])
            plt.xlim(xmax=0.4)
            plt.legend()               
            plt.show()
            
            
    def get_distanse_between_author(self, filename):
        self.get_distance()
        distance = dict()   
        for author in self.authors:
            distance[author.get_name()] = list()
            for other in self.authors:
                distance[author.get_name()].append(sum(np.absolute(author.get_author_pfr() - other.get_author_pfr())))
        result_file = open(filename,'a')
        for a, d in distance.items():
                result_file.write('{0:15} | {1}'.format(a,d)+'\n')        
        result_file.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        result_file.close()      
                
                 
                
            
            
        
        

            
            
            
        
        

   
   
            
  
                
               
        
        

        