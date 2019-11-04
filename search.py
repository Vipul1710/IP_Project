import numpy as np
import csv
import cv2
import urllib.request
from Final_file import ColorDescriptor
from searcher import Searcher

with open("D:/TRF IP TASK/image search/train1.csv",'r') as csvfile:
    reader = csv.reader( csvfile, delimiter=',' )
    list1=list(reader)         
cd = ColorDescriptor((8, 12, 3))
query = cv2.imread("D:/PHOTOS/BANGALORE,MYSORE/land.jpg")
features = cd.describe(query)
 
# perform the search
csvfile=open('D:/TRF IP TASK/output2.csv', 'r')
searcher = Searcher()
results = searcher.search(features)
 
# display the query
query1=cv2.resize((query),(500,500))
cv2.imshow("Query", query1)
 
# loop over the results
s="0"
column=0
try:
    for (score, resultID) in results:
    	# load the result image and display it
    	source=urllib.request.urlopen(list1[int(resultID)][column])
    	array=np.array(bytearray(source.read()),dtype=np.uint8)
    	img1=cv2.imdecode(array,-1)
    	result=cv2.resize(img1,(200,200))
    	cv2.imshow(s,result)
    	s=chr(ord(s)+1)
except:
    pass        
cv2.waitKey(0)
cv2.destroyAllWindows()

