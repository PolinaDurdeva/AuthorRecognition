#-*- coding: utf-8 -*-
import string
import os
import Constants

class CleaningText():

    def __init__(self, text=None, filename = None):
        self.text = text
        self.clean_text()        
        self.filename = filename
        
    def get_text(self):
        return self.text
    
    def get_filename(self):
        return self.filename
    
    def clean_text(self):
        #self.text = self.text.decode('utf8')
        self.text = self.lower_text()
        if (Constants.language == 'ru'):       
            self.text = self.remove_for_ru()
        else:
            self.text = self.remove_for_eng()
        #self.text = self.text.encode('utf8')
        
    def remove_for_eng(self):
        return filter(lambda x: x in string.ascii_letters, self.text)
            
    def lower_text(self):
        return self.text.lower()    
    
    def remove_for_ru(self):
        alf = u"абвгдеёжздийклмнопрстуфхцчщшъьюяыэ"
        return filter(lambda x: x in alf, self.text)
        
    def put_in_file(self, path_name): 
        new_file = open(os.path.join(path_name,self.filename),'w')
        new_file.write(self.text.encode('utf8'))
        new_file.close()
   
        