#-*- coding: utf-8 -*-
import Constants
import os
import numpy as np


#import string
class Book():
    
    def __init__(self,filename = None, text = None, Ngramm = 3):
        self.text = text
        self.N = Ngramm
        self.real_author = ""
        self.name = ""
        ##
        self.ngramms = dict()
        self.PFR = list()
        self.create_dictionary()
        self.calculate_pfr()
        self.distance = dict()
        self.stationary_len = list()
        self.stationary_level = list()
        ##
        if (self.text != None):
            self.set_book_description(filename)     
               
    def get_N(self):
        return self.N   
    
    def get_length(self):
        return len(self.text)
        
    def get_author(self):
        return self.real_author  
          
    def get_name(self):
        return self.name
    
    def get_ngramms(self):
        return self.ngramms
    
    def get_pfr(self):
        return np.array(self.PFR) 
    
    def get_distance(self):
        return self.distance
    
    def get_near_author(self):
        min_dist = 10000
        for k, v in self.distance.iteritems():
            if (v < min_dist):
                min_dist = v
                author = k
        return author
    
    def get_stationary_len(self):
        return self.stationary_len, self.stationary_level
     
    def set_book_description(self, filename):
        info = filename.split(' ')
        self.real_author = info[0]
        self.name = info[1].split('.')[0]
        self.length = self.get_length()
          
    def get_book_description(self):
        return self.real_author + ' ' + self.name + ' ' + str(self.length)
                
    def create_dictionary(self): 
        for i in range(0, self.get_length(), self.N):
            piece = self.text[i : i + self.N]
            if self.ngramms.has_key(piece):
                self.ngramms[piece] +=1
            else:
                self.ngramms[piece] = 1        
        print 'dictionary(ngramms) is created'
    
    def calculate_pfr(self):
        num_ngram = self.get_length()/self.N
        for gram in Constants.set_pfr:
            if self.ngramms.has_key(gram):                
                self.PFR.append(float (self.ngramms[gram])/num_ngram)
            else:
                self.PFR.append(0) 
        
    def calculate_similarity(self, author):
        dist = sum(np.absolute(self.get_pfr() - author.get_avg_pfr()))
        self.distance[author.get_name()] = dist
        
    
    def calculate_proximity(self, author):
        count_gramm = self.get_length()/self.get_N()
        coeff = float(count_gramm)/author.get_sum_gramm()
        author_pfr = (author.get_avg_pfr() - self.get_pfr()*coeff)/(1-coeff)
        dist = sum(np.absolute(self.get_pfr() - author_pfr))
        self.distance[author.get_name()] = dist
           
    def get_min_distance(self):
        return min(self.distance)
                
    def print_dict_in_file(self,path):
        file_name = self.get_book_description() + '.txt'
        new_file = open(os.path.join(path,file_name),'w')
        for key in self.ngramms.keys():
            new_file.write(str(key.encode('utf8')) + ' '+ str(self.ngramms[key]) + '\n')        
        new_file.close()
    
    def print_book_description_in_file(self,path):
        info_file = open(path, 'a')
        info_file.write('{0:15}  {1:30}  {2}  {3}'.format(self.real_author,self.name, self.length, str(len(self.ngramms))+'\n') )
        info_file.close()
         
################
    def c_dict(self, text): 
        ngramms = dict()
        for i in range(0, len(text), self.N):
            piece = text[i : i + self.N]
            if ngramms.has_key(piece):
                ngramms[piece] +=1
            else:
                ngramms[piece] = 1
        return ngramms
        
    def c_pfr(self,length,ngramms):
        pfr = list()
        num_ngram = length/self.N
        for gram in Constants.set_pfr:
            if ngramms.has_key(gram):
                pfr.append(float (ngramms[gram])/num_ngram)
            else:
                pfr.append(0) 
        return np.array(pfr)      
      
    def calculate_stationary_length(self):
        l = 0
        step = 5000
        while (l < 800000):
            l += step
            if (len(self.text)< l):
                break
            if (l > 100000):
                step = 20000
            cut_txt = self.text[0:l]
            gram = self.c_dict(cut_txt)
            pfr = self.c_pfr(l,gram)
            dist = sum(np.absolute(self.PFR - pfr))
            self.stationary_len.append(l)
            self.stationary_level.append(round(dist,2))
        return len
            
    def print_stat_len(self,filename):
        info_file = open(filename, 'a')
        info_file.write('{0:15}  {1:30}'.format(self.name,self.real_author)+'\n')
        for l in range(len(self.stationary_len)):
            info_file.write('{0}  {1}'.format(self.stationary_len[l],self.stationary_level[l])+'\n' )
        info_file.close()
               
          