import numpy as np
import csv



class Searcher:
	def search(self, queryFeatures, limit = 1):
		results = {} 
		csvfile=open('D:/TRF IP TASK/output2.csv', 'r')
		reader = csv.reader(csvfile)
	
		for row in reader:
				
				# parse out the image ID and features, then compute the
				# chi-squared distance between the features in our index
				# and our query features
				try:                    
				    features = [float(x) for x in row]
				except ValueError:
				    pass
				d = self.chi2_distance(features, queryFeatures)				
				
				results[row[0]] = d
		csvfile.close()    
		results = sorted([(v, k) for (k, v) in results.items()]) 
		return results[:limit]
    
	def chi2_distance(self, histA, histB, eps = 1e-10):
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
		return d