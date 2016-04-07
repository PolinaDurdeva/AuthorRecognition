import numpy as np
import random

class PamCluster(object):

    def __init__(self, books, K):
        self.K = K
        self.books = books
        self.distance_matrix = list()
        self.clusters = dict()
        
    def get_clusters(self):
        return self.clusters
    
    def distance_between_pfr(self,pfr,other_pfr):
        dist = sum(np.absolute(np.array(pfr) - np.array(other_pfr)))
        return dist
        
    def create_distance_matrix(self):
        for book in self.books:
                book_dist = list()
                for other_book in self.books:
                    book_dist.append(self.distance_between_pfr(book.get_pfr(), other_book.get_pfr()))
                self.distance_matrix.append(book_dist)
                
    def spread_to_clusters(self, distances, k=4):
        m = distances.shape[0] # number of points
        print m
    
        # Pick k random medoids.
        curr_medoids = np.array([-1]*k)
        while not len(np.unique(curr_medoids)) == k:
            curr_medoids = np.array([random.randint(0, m - 1) for _ in range(k)])
        old_medoids = np.array([-1]*k) # Doesn't matter what we initialize these to.
        new_medoids = np.array([-1]*k)
        
        # Until the medoids stop updating, do the following:
        while not ((old_medoids == curr_medoids).all()):
            # Assign each point to clusters with closest medoid.
            clusters = self.assign_points_to_clusters(curr_medoids, distances)
            
            # Update clusters medoids to be lowest cost point. 
            for curr_medoid in curr_medoids:
                cluster = np.where(clusters == curr_medoid)[0]
                new_medoids[curr_medoids == curr_medoid] = self.compute_new_medoid(cluster, distances)
    
            old_medoids[:] = curr_medoids[:]
            curr_medoids[:] = new_medoids[:]
        
        
        return clusters, curr_medoids

    def assign_points_to_clusters(self,medoids, distances):
        distances_to_medoids = distances[:,medoids]
        clusters = medoids[np.argmin(distances_to_medoids, axis=1)]
        clusters[medoids] = medoids
        return clusters

    def compute_new_medoid(self, cluster, distances):
        mask = np.ones(distances.shape)
        mask[np.ix_(cluster,cluster)] = 0.
        cluster_distances = np.ma.masked_array(data=distances, mask=mask, fill_value=10e9)
        costs = cluster_distances.sum(axis=1)
        return costs.argmin(axis=0, fill_value=10e9)
    
    def start_clustering(self):
        self.create_distance_matrix()
        clusters, curr_medoids = self.spread_to_clusters(np.array(self.distance_matrix), self.K)
        self.create_clusters(clusters, curr_medoids)
        self.print_results()
    
    def create_clusters(self, clusters, medoids):
        for medoid in medoids:
            self.clusters[medoid] = list()
        for cl in range(len(clusters)):
            self.clusters[clusters[cl]].append(self.books[cl])
            
    def print_results(self):
        for key, cl in self.clusters.items():
            print "CLUSTR\n",key
            for book in cl:
                print '{0:15}  {1:30}'.format(book.get_author(), book.get_name())+'\n'
            
        
           
