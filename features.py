from Final_file import ColorDescriptor
import csv
import urllib.request
import cv2
import numpy as np


column=0
with open("D:/TRF IP TASK/image search/train1.csv",'r') as csvfile:
    reader = csv.reader( csvfile, delimiter=',' )
    list1=list(reader)
    
column=0
s="0"
csvfile=open('D:/TRF IP TASK/output.csv', 'a')
cd = ColorDescriptor((8, 12, 3))
j=1
for i in range(0,1001):
    try:
        source=urllib.request.urlopen(list1[i][column])
        array=np.array(bytearray(source.read()),dtype=np.uint8)
        img1=cv2.imdecode(array,-1)
        #img2=cv2.resize(img1,(200,200))
        #cv2.imshow(s,img2)
        #s=chr(ord(s)+1)
        print(i)
        features = cd.describe(img1)
        features = [str(f) for f in features]
        csvfile.write("%s,%s\n" % (str(i), ",".join(features)))
        
    except urllib.request.HTTPError:
        del list1[i][0]
        continue
    except ValueError:
        del list1[i][0]
        continue
    except :
        del list1[i][0]
        continue
        
csvfile.close()   
#cv2.waitKey(0) 
#cv2.destroyAllWindows()

