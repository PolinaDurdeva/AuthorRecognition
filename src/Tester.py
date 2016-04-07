#-*- coding: utf-8 -*-
from CleaningTextMaster import CleaningText
from BookModule import Book
import Constants
import os
import codecs
from LibraryModule import Library
from KmeansClustering import KMeans
from PAMClustering import PamCluster
from GlobalKmeansClustering import GlobalKmeans
from ClassificationModule import Classification
from ClusteringProcess import ClusterMaster


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
    
        
def test_kmeans():
    lib = Library(cleaning=False)
    lib.load_clustring_clean_books(Constants.cluster_path)
    kmeams_cl = KMeans(lib.get_books(), 6)
    kmeams_cl.start_clustering()
    kmeams_cl.print_results()
    cluster_master = ClusterMaster()
    cluster_master.expertize(6, kmeams_cl.get_clusters(), lib.get_authors())
        
def test_pam():
    lib = Library(cleaning=False)
    lib.load_clustring_clean_books(Constants.cluster_path)
    pam_cl = PamCluster(lib.get_books(), 3)
    pam_cl.start_clustering()
    cluster_master = ClusterMaster()
    cluster_master.expertize(3, pam_cl.get_clusters(), lib.get_authors())
    
def test_gkm():
    lib = Library(cleaning=False)
    lib.load_clustring_clean_books(Constants.cluster_path)
    gkm_cl = GlobalKmeans(lib.get_books(), 3)
    gkm_cl.start_clustering()
    gkm_cl.print_results()
    cluster_master = ClusterMaster()
    cluster_master.expertize(3, gkm_cl.get_clusters(), lib.get_authors())
         
def test_classification():
    cl = Classification(True)
    cl.start_classification()
    
def test_statistics():
    cl = Classification(False)
    cl.collect_statistics()

    
       

    
    
    