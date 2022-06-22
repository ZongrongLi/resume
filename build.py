import os
import re
import sys
import traceback
import collections
import shutil

movdir = r"./"
basedir = r"./public/"

for root, dirs, files in os.walk(movdir):
    for filename in files:
        #print(filename)
        if "dacc134df843c368a5bd" in filename:
                os.remove(filename)
                
                
for root, dirs, files in os.walk(basedir):
    for filename in files:
         if "component---src-pages-index-tsx" in filename:
            originname = filename[::]
            ss= filename.split('-') 
            s1 = ss[7].split('.')
            newfilename = filename.replace(s1[0],"dacc134df843c368a5bd")
            print("copy=====>>",filename)
            shutil.copy(basedir+filename,movdir+newfilename)
            os.remove(basedir+filename)
            
            
