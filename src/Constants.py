import Utils
import os

language = 'ru'
#language = 'en'
set_pfr = Utils.get_set_pfr(language)
#Directories
data_path = os.path.join(os.getcwd(), "..", "Data")
ngrams_path = os.path.join(data_path, "Ngramms")
classif_dirty_book_path = os.path.join(data_path,"ClassificationRUDirty")
classif_clean_book_path = os.path.join(data_path,"ClassificationRUClean")
cluster_path = os.path.join(data_path,"ClusteringCleanBook")
#classif_dirty_book_path = os.path.join(data_path,"ClassificationDirtyBook")
#classif_clean_book_path = os.path.join(data_path,"ClassificationCleanBook")
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