# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:07:34 2016

@author: Nestor
"""
#############################################
#  DOWNLOADING PDF FILES FROM NIPS WEBSITE  #
#############################################

from bs4 import BeautifulSoup
import requests
import os


# IMPORTANT NOTICE!!! Change the next path with the desired one if you want to launch the code, here and in the "pdfFile =" instruction
os.makedirs('C:/Users/Nestor/Desktop/_/NIPS 2016/papers', exist_ok=True) 

url = ("http://papers.nips.cc/book/advances-in-neural-information-processing-systems-29-2016")
# Download the page.
soup = BeautifulSoup(requests.get(url).text, "lxml")
esto = soup.select('ul > li > a[href*="paper"]') #all Tags (inside a Tag li inside a Tag ul) with href attribute containing the string "paper"

for i in range(esto.__len__()):
    link = esto[i].get('href')
    link = 'http://papers.nips.cc' + esto[i].get('href') + ".pdf"
    res = requests.get(link)
    # Save the image to ./xkcd.
    pdfFile = open(os.path.join('C:/Users/Nestor/Desktop/_/NIPS 2016/papers', os.path.basename(link)), 'wb')
    for chunk in res.iter_content(100000):
        pdfFile.write(chunk)
        
    pdfFile.close()
    
