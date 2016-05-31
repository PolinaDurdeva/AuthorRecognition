import random
import numpy as np
import Constants

class KMeans(object):
    def __init__(self,books,K,centroids=None):
        self.books = books
        self.K = K
        self.centroids = centroids
        self.clusters = dict()
        
    def initialize_all_objects(self):
        self.centroids = list()
        self.initialize_clusters()
        random_centers = random.sample(self.books, self.K)
        self.centroids = np.array([b.get_pfr() for b in random_centers])
          
    def get_centroids(self):
        return self.centroids
    
    def get_clusters(self):
        return self.clusters
    
    def initialize_clusters(self):   
        for k in range(self.K):
            self.clusters[k]= list()
            
    def rebuild_representer(self):
        new_centroids = list()
        for spread_to_clusters in self.clusters.values():
            if (len(spread_to_clusters) == 0):
                continue
            sum_gr = 0   
            lenght = len(Constants.set_pfr)
            sum_pfr = np.zeros(lenght)
            for book in spread_to_clusters:
                #count_ngramm = book.get_length()/book.get_N()
                count_ngramm = book.get_length()
                tmp = book.get_pfr()* count_ngramm
                sum_pfr += tmp          
                sum_gr += count_ngramm
            avg_pfr = np.array(sum_pfr)/sum_gr
            new_centroids.append(avg_pfr)
        check = not np.array_equal(self.centroids,new_centroids)
        self.centroids = new_centroids
        return check
    
    def spread_to_cluster(self):        
        self.clusters.clear()      
        self.initialize_clusters()                   
        for book in self.books:
            i = 0
            min_distance = 10000
            for centr in self.centroids:
                dist = sum(np.absolute(book.get_pfr() - np.array(centr)))
                if (dist < min_distance):
                    min_distance = dist
                    cl = i
                i+=1
            self.clusters[cl].append(book)   
            
    def get_cost(self):
        cost = 0
        for key, spread_to_clusters in self.clusters.items():
            for book in spread_to_clusters:
                dist = sum(np.absolute(book.get_pfr() - np.array(self.centroids[key])))
                cost += dist**2
        return cost
               
    def start_clustering(self):
        max_iter=40
        if self.centroids == None:
            self.initialize_all_objects()
        check = True
        i = 0
        while check and (i < max_iter):
            self.spread_to_cluster()
            check = self.rebuild_representer()
            i+=1             
            print 'itter:',i
        self.spread_to_cluster()
        print "check:", check           
        
    def print_results(self):
        for key, cl in self.clusters.items():
            print "CLUSTR\n",key
            for book in cl:
                print '{0:15}  {1:30}'.format(book.get_author(), book.get_name())+'\n'   
        