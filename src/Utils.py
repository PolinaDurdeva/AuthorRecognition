#-*- coding: utf-8 -*-
import string
import re
import datetime
import os

def get_safe_time_string():
    return str(datetime.datetime.now()).replace(":","-")[:-10]

def get_set_pfr(language):
    print "SUPER WORK"
    set_pfr = list()
    if (language == u'en'):
        alf = string.ascii_letters
    elif (language == u'ru'):
        alf = u"абвгдежзийклмнопрстуфхцчшщъьюыэя"
    elif (language == u'ger'):
        alf = u"qwertyuiopasdfghjklzxcvbnmäöüß"
    for l in alf:
        for w in alf:
            for z in alf:
                set_pfr.append(l+w+z)
    return set_pfr
    
def remove_eng_letters(text):
        print 'remove eng_letters in book'
        for c in string.ascii_lowercase:
            text = text.replace(c,"") 
        return text
    
def remove_num(text):
    print 'remove numbers in book'
    for c in string.digits:
        text = text.replace(c,"") 
    return text    
           
def remove_punctuation(text):
    print 'remove punctuation in book'
    for c in string.punctuation:
        text = text.replace(c,"")    
    text = text.decode('utf8').replace(u"\u2014", u"") 
    text = text.replace(u"\u2013", u"")
    text = text.replace(u"\u2026", u"")
    text = text.replace(u"\u00ab", u"") 
    text = text.replace(u"\u00bb", u"")  
    text = re.sub('\s+', ' ', text)
    
    return text

def remove_for_eng(text):
    text = filter(lambda x: x in string.ascii_letters, text)
    return text
        
def lower_text(text):
    text = text.lower()
    return text

def remove_space(text):
    print 'remove spaces' 
    text = text.replace(' ', "")
    return text
def clean_dir(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path,f))

def cut_text(text,len):
    return text[0:len]       

