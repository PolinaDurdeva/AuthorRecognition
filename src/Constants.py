#-*- coding: utf-8 -*-
import Utils
import os

#language = 'ru'
#language = 'en'
books_language = 'ru'
ru_alfa = u"абвгдеёжзийклмнопрстуфхцчщшъьюяыэ"
german_alfa = u"qwertyuiopasdfghjklzxcvbnmäöüß"
set_pfr = Utils.get_set_pfr(books_language)
#Directories
data_path = os.path.join(os.getcwd(), "..", "Data")
ngrams_path = os.path.join(data_path, "Ngramms")
library_path = os.path.join(data_path, "Library")
clean_library = os.path.join(library_path, "clean")
dirty_library = os.path.join(library_path, "dirty")
statinary_len_path = os.path.join(data_path,"StationaryLength")
#Files
statistics_filepath = os.path.join(data_path,"Statistics.txt")
results_filepath = os.path.join(data_path,"Results.txt")
stat_lenght_filepath = os.path.join(data_path,"StatLen.txt")
classif_info_filepath = os.path.join(data_path,"ClassificationInfo.txt")


#####
#library_path = os.path.join(data_path, "SampleText")
#clean_text_path= os.path.join(data_path, "CleanText")
#train_path = os.path.join(data_path, "Train")
#clean_train_path = os.path.join(data_path, "CleanTrain")
