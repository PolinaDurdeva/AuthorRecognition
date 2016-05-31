from KmeansClustering import KMeans
import numpy as np
from math import factorial

class GlobalKmeans(object):

    def __init__(self, books,K):
        self.centroids = list()
        self.books = books
        self.K = K
        self.clusters = dict()
        self.kmeans_cl = KMeans(self.books, 1)
    
                         
    def start_clustering(self):
        self.kmeans_cl.start_clustering()   
        for i in range(2,self.K+1):
            cost = 1000
            self.centroids = self.kmeans_cl.get_centroids()
            for book in self.books:
                self.centroids.append(book.get_pfr())
                self.kmeans_cl = KMeans(self.books, i, self.centroids)
                self.kmeans_cl.start_clustering()
                new_cost = self.kmeans_cl.get_cost()
                #print "cost:", new_cost
                if (new_cost < cost):
                    best_book = book
                    cost = new_cost    
                self.centroids.pop()
            print "final cost", cost
            self.centroids.append(best_book.get_pfr())
            self.kmeans_cl = KMeans(self.books, i, self.centroids)
            self.kmeans_cl.start_clustering()
    
    def print_results(self):
        self.kmeans_cl.print_results()
        
    def get_clusters(self):
        return self.kmeans_cl.get_clusters()     
        
            

        