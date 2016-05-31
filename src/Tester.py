#-*- coding: utf-8 -*-
from LibraryModule import Library
from KmeansClustering import KMeans
from PAMClustering import PamCluster
from GlobalKmeansClustering import GlobalKmeans
from ClassificationModule import Classification
from ClusteringProcess import ClusterMaster
import Utils
from Statistics import Statistics


'''def test_book():
    path = os.listdir(Constants.library_path)[0]
    text = codecs.open(os.path.join(Constants.library_path,path), 'r',"utf-8")
    txt = text.read()
    clean_text=CleaningText(text=txt,filename=u'Turgenev Mumu')
    print clean_text.get_filename()
    print clean_text.get_text()
    book = Book(text=clean_text.get_text(),filename=clean_text.get_filename())
    print "ngrans: ", book.get_ngramms()
    print "pfr: ", book.get_pfr()'''
    
        
def test_kmeans(language, authors, clean):
    lib = Library(cleaning=clean)
    lib.load_library(language)
    cluster_master = ClusterMaster()
    kmeams_cl = KMeans(lib.get_books(), authors)
    kmeams_cl.start_clustering()
    kmeams_cl.print_results()
    cluster_master.expertize(authors, kmeams_cl.get_clusters(), lib.get_authors_name())
    kmeams_cl = KMeans(lib.get_books(), authors)
    kmeams_cl.start_clustering()
    kmeams_cl.print_results()
    cluster_master.expertize(authors, kmeams_cl.get_clusters(), lib.get_authors_name())
    kmeams_cl = KMeans(lib.get_books(), authors)
    kmeams_cl.start_clustering()
    kmeams_cl.print_results()
    cluster_master.expertize(authors, kmeams_cl.get_clusters(), lib.get_authors_name())
    kmeams_cl = KMeans(lib.get_books(), authors)
    kmeams_cl.start_clustering()
    kmeams_cl.print_results()
    cluster_master.expertize(authors, kmeams_cl.get_clusters(), lib.get_authors_name())
 
def test_pam(language, authors, clean):
    lib = Library(cleaning=clean)
    lib.load_library(language)
    pam_cl = PamCluster(lib.get_books(), authors)
    cluster_master = ClusterMaster()
    cluster_master.expertize(authors, pam_cl.get_clusters(), lib.get_authors_name())
    
def test_gkm(language, authors, clean):
    lib = Library(cleaning=clean)
    lib.load_library(language)
    gkm_cl = GlobalKmeans(lib.get_books(), authors)
    gkm_cl.start_clustering()
    gkm_cl.print_results()
    cluster_master = ClusterMaster()
    cluster_master.expertize(authors, gkm_cl.get_clusters(), lib.get_authors())
         
def test_classification(clean=False, language='en'):
    lib = Library(cleaning=clean)
    lib.load_library(language=language)
    cl = Classification(language=language, books=lib.get_books(),authors=lib.get_authors())
    cl.start_classification()
    #st = Statistics(books=lib.get_books(),authors=lib.get_authors())
    #st.get_avg_len_of_books()
    
    
def test_statistics(clean=False, language='en'):
    lib = Library(cleaning=clean)
    lib.load_library(language=language)
    st = Statistics(books=lib.get_books(),authors=lib.get_authors())
    st.collect_statistics()
    #st.get_avg_len_of_books()
    #cl.get_distanse_between_author(Constants.results_filepath)
    
def test_stationary_len(clean=False, language='en'):
    lib = Library(cleaning=clean)
    lib.load_library(language=language)
    cl = Classification(language=language, books=lib.get_books(),authors=lib.get_authors())
    cl.drow_stat_len()

def test_accuracy(clean=False, language='en'):
    lib = Library(cleaning=clean)
    lib.load_library(language=language)
    l=10000
    while (l > 0):
        print l
        for book in lib.get_books():
            book.set_new_text(text=Utils.cut_text(book.get_text(), l))
        cl = Classification(language=language, books=lib.get_books(),authors=lib.get_authors())
        cl.start_classification()
        if (l>5000): 
            l -= 50000
        else:
            l -= 1000 
        
    
    
       

    
    
    