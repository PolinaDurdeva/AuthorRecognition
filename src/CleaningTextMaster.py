#-*- coding: utf-8 -*-
import string
import os
import Constants

class CleaningText():

    def __init__(self, lang="ru", text=None, filename = None):
        self.text = text             
        self.filename = filename
        self.language = lang
        print self.language
        self.clean_text()
        
    def get_text(self):
        return self.text
    
    def get_filename(self):
        return self.filename
    
    def clean_text(self):
        #self.text = self.text.decode('utf8')
        self.text = self.text.lower()
        if (self.language == "ru"):  
            print "Russian language"     
            self.text = self.remove_for_ru()
            self.text = self.text.replace(u'ё',u'e')
        elif (self.language == 'ger'):
            print "German language"
            self.text = self.remove_for_german()
        elif (self.language == 'en'): 
            print "English language"   
            self.text = self.remove_for_eng()
        else:
            print "NO language"
                       
        #self.text = self.text.encode('utf8')
        
    def remove_for_eng(self):
        return filter(lambda x: x in string.ascii_letters, self.text)

    def remove_for_ru(self):
        return filter(lambda x: x in Constants.ru_alfa, self.text)
    
    def remove_for_german(self):
        return filter(lambda x: x in Constants.german_alfa,self.text)
    
    def put_in_file(self, path_name): 
        new_file = open(os.path.join(path_name,self.filename),'w')
        new_file.write(self.text.encode('utf8'))
        new_file.close()
   
        