#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from AuthorModule import Author
import numpy as np

class Statistics():

    def __init__(self, books = None, authors = None):
        self.books = books
        self.authors_name = authors
        self.step = 0.05
        ##
        self.count_book = len(self.books)
        self.count_author = len(self.authors_name)
        ##
        self.distance_s = list()
        self.distance_o = list()
        self.dist_between_books = list()
        
    def distance_between_pfr(self,pfr,other_pfr):
        dist = sum(np.absolute(np.array(pfr) - np.array(other_pfr)))
        return dist 
             
    ## Расстояние от книги до чужого авторского представителя 
    def collect_distance_s(self):
        for book in self.books:
            for author in self.authors_name:
                if (book.get_author() != author):
                    self.distance_s.append(self.distance_between_pfr(book.get_pfr(), author.get_avg_pfr()))   
    
    ## Расстояние между книгами                    
    def collect_dist_between_books(self):
        for book in self.books:
            for other in self.books:
                if (book.get_name() != other.get_name()):
                    self.dist_between_books.append(self.distance_between_pfr(book.get_pfr(), other.get_pfr())) 
                    
    ## Расстояние от книги до своего авторского представителя            
    def collect_disttance_o(self):
        for author in self.authors_name:
            for book in author.get_books():
                count_gramm = book.get_length()/book.get_N()
                coeff = float(count_gramm)/author.get_sum_gramm()
                author_pfr = np.array((author.get_avg_pfr() - book.get_pfr()*coeff))/(1-coeff)
                dist = self.distance_between_pfr(book.get_pfr(), author_pfr)/(1-coeff)
                self.distance_o.append(dist)
                
        
    def pdf(self,arr):
        return np.histogram(arr, bins=np.arange(0,1.05, self.step))
    
    def cdf(self, histogram):
        distribution = list()
        sum = 0
        for i in histogram:
            distribution.append(sum)
            sum+=i
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
        while (i < lenght) and (arr[i] < 0.999):
            p+=self.step
            i+=1
        return p
    
    def h1_error(self,arr, pmin):
        index = int( pmin / self.step)
        return arr[index]
    
    def h2_error(self,arr,pmax):
        index = int( pmax / self.step)
        return 1 - arr[index]
    
    def p_separation(self,arr1, arr2):
        max=0
        ind = -1
        for i in range(len(arr1)):
            sum = arr1[i] + arr2[i]
            if (sum > max):
                max = sum
                ind = i
        return ind*self.step
    
    def collcet_statistic(self):
        self.collect_distance_s()
        self.collect_disttance_o()
        pdf_s, xs = self.pdf(self.distance_s)
        self.grafic_show(np.array(pdf_s)/float(len(self.distance_o)), xs, 'ddd')
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
        #info_file = open(filename, 'a')
        print cdf_o
        print cdf_s
        print 'pmin= ', pmin, ' pmax = ', pmax, ' p sep = ', p_sep
        print 'h1 error = ', h1_error, ' h2_error = ', h2_error
        print 'mean other = ', mean_o, " mean self = ", mean_s  
        print 'std other = ', std_o, " std self = ", std_s 
        

            
    def grafic_show(self, arr, bins, title):
        plt.ylabel(u'Вероятность')
        plt.xlabel(u"Расстояние")
        plt.title(title)
        plt.grid(True)
        plt.hist(arr, bins = bins, normed=True)  # plt.hist passes it's arguments to np.histogram
        plt.show()
            
        
        

            
            
            
        
        

   
   
            
  
                
               
        
        

        