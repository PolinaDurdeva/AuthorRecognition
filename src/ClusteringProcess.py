import numpy as np
from math import factorial
 
class ClusterMaster(object):

    def __init__(self):
        print "cluster master is created"
     
    def evaluate_cluster_matrix(self,clusters_matrix, debug = True):                
        clusters_matrix = np.array(clusters_matrix)
        number_of_cluster = clusters_matrix.shape[0]
        number_of_class = clusters_matrix.shape[1]
        count_of_elements = clusters_matrix.sum()
        count_of_pairs = count_of_elements * (count_of_elements - 1) / 2
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0
        total_positive = 0
        total_negative = 0
        combinations  = lambda n: factorial(n) / (2 * factorial(n - 2)) if n > 2 else 1 if n == 2 else 0 
        # compute true positive
        for elem in clusters_matrix.flat:
            true_positive += combinations (elem)
        #compute false positive
        for row in clusters_matrix:
            total_positive += combinations(row.sum())     
        false_positive  = total_positive - true_positive        
        #compute false negative        
        for i in range(number_of_class):
            column = clusters_matrix[:,i]
            final_sum = 0
            for i in range(number_of_cluster):
                for j in range(1 + i, number_of_cluster):
                    final_sum += column[i] * column[j]
            false_negative += final_sum          
        #compute true negative
        total_negative = count_of_pairs - total_positive
        true_negative = total_negative - false_negative  
        #compute precision and recall
        precision = float(true_positive) / total_positive
        recall = float(true_positive) / (true_positive + false_negative)      
        #compute F-measure
        alfa = 1
        f_measure = float(1 + alfa) / (float(1) / precision + float(alfa) / recall)
        #compute Rand Index
        rand_index = float(true_negative + true_positive) / (total_positive + total_negative)  
        #compute purity 
        purity = float(1) / count_of_elements * clusters_matrix.max(axis = 1).sum()
        #compute NMI
        mutual_information = 0
        entropy_cluster = 0
        entropy_class = 0
        for i in range(number_of_class):
            #count of elements in i cluster
            ci_elem_count = clusters_matrix[i,:].sum()
            if ci_elem_count > 0 :
                entropy_cluster -= float(ci_elem_count) / count_of_elements * np.log(float(ci_elem_count) / count_of_elements)
                for j in range(number_of_cluster):
                    #count of elements in i class (count of elements of one author)
                    cli_elem_count = clusters_matrix[:,j].sum()
                    element = clusters_matrix[i,j]
                    if (cli_elem_count > 0 and element > 0) :                   
                        tmp = np.log(float(count_of_elements * element) / (ci_elem_count * cli_elem_count))
                        mutual_information += float(element) / count_of_elements * tmp
        for j in range(number_of_class):
            cli_elem_count = clusters_matrix[:,j].sum()
            if cli_elem_count > 0: 
                entropy_class -= float(cli_elem_count) / count_of_elements * np.log(float(cli_elem_count) / count_of_elements)
        nmi = float(mutual_information) / (0.5 * (entropy_class + entropy_cluster))                      
        evaluating = [precision,recall,purity,f_measure,rand_index,nmi]
        if debug:
            print "*****CLUSTER MATRIX*****"
            print clusters_matrix
            print "True Positive = ", true_positive
            print "True Negative = ", true_negative
            print "False Positive = ", false_positive
            print "False Negative = ", false_negative   
            print "Precision, Recall, Purity, F-measure, Rand Index, NMI"
            print evaluating      
        return evaluating
    
    def get_author_in_cluster(self,author,books):
        return len(filter(lambda x: x.get_author()== author ,books))
            
    def expertize(self, K, clusters, authors, debug=False):
        cluster_map = clusters
        print "*** Expertize:(TF,IDF,F-MEASURE,Rand Index,Purity,NMI) ***"
        #Printing all clusters
        if debug:
            print "debug"           
        clusters_matrix = []
        for books in cluster_map.values():
            clusters_matrix.append(map(lambda x: self.get_author_in_cluster(x, books), authors))
        self.statistic_evaluation = self.evaluate_cluster_matrix(clusters_matrix,False)
        print self.statistic_evaluation
        return self.statistic_evaluation   