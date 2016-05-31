#-*- coding: utf-8 -*-
from Tester import *
from Constants import books_language

#!!!
#select the desired language in the constants module
#!!!
#test_kmeans(language=books_language,authors=10,clean=False)
#test_gkm(language=books_language,authors=5,clean=False)
test_classification(clean=False, language=books_language)
#test_stationary_len(language=books_language)
#test_pam(language=books_language,authors=5,clean=False)
#test_accuracy(clean=False, language=books_language)
#test_statistics(False, language=books_language)


