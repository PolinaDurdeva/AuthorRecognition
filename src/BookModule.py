#-*- coding: utf-8 -*-
import Constants
import os
import numpy as np


#import string
class Book():
    
    def __init__(self,author, name = None, text = None, Ngramm = 3):
        self.text = text
        self.N = Ngramm
        self.real_author = author
        self.name = name
        ##
        self.set_length()
        self.ngramms = dict()
        self.PFR = list()
        self.create_dictionary()
        self.calculate_pfr()
        self.distance = dict()
        self.stationary_length = dict()
        ##
                       
    def get_text(self):
        return self.text
     
    def set_new_text(self, text):
        self.text = text
        self.set_length()
        self.ngramms = dict()
        self.PFR = list()
        self.create_dictionary()
        self.calculate_pfr()
        self.distance = dict()
               
    def set_length(self):
        self.length = len(self.text)
                      
    def get_N(self):
        return self.N   
    
    def get_length(self):
        return self.length
        
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
        return self.stationary_length, self.stationary_level
     
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
        for gram in Constants.set_pfr:
            if self.ngramms.has_key(gram):
                self.PFR.append(float (self.ngramms[gram])/self.get_length()) 
            else:
                self.PFR.append(0) 
                
    #distance to the stranger author    
    def calculate_similarity(self, author):
        dist = sum(np.absolute(self.get_pfr() - author.get_author_pfr()))
        self.distance[author.get_name()] = dist
        
    #the distance to its author
    def calculate_proximity(self, author):
        coeff = float(self.length)/author.get_sum_gramm()
        dist = sum(np.absolute(self.get_pfr() - author.get_author_pfr()))/(1-coeff)
        self.distance[author.get_name()] = dist
           
    def print_ngramms_in_file(self,path):
        file_name = self.get_book_description() + '.txt'
        new_file = open(os.path.join(path,file_name),'w')
        for key in self.ngramms.keys():
            new_file.write('{0} {1}'.format(str(key.encode('utf8')),str(self.ngramms[key]) + '\n'))        
        new_file.close()
    
    def print_book_description_in_file(self,path):
        info_file = open(path, 'a')
        info_file.write('{0:15}  {1:30}  {2}  {3}'.format(self.real_author,self.name, self.length, str(len(self.ngramms))+'\n') )
        info_file.close()
   
   
   
   #TODO: stationary length of text      
################     
      
    def calculate_stationary_length(self):
        step = 1000
        length_text = self.length
        old_pfr = self.PFR
        while (length_text > 0):          
            length_text -= step
            cut_txt = self.text[0:length_text]
            self.set_new_text(cut_txt)
            dist = sum(np.absolute(old_pfr - self.PFR))
            self.stationary_length[length_text] = round(dist,3)
                    
    def print_stationary_length_in_file(self,filename):
        info_file = open(filename, 'a')
        info_file.write('{0:15}  {1:30}'.format(self.name,self.real_author)+'\n')
        for key, value in self.stationary_length.items():            
            info_file.write('{0}  {1}'.format(key, value+'\n' ))
        info_file.close()
               
          