import requests
from bs4 import BeautifulSoup
import os
import time
import json

baseurl = 'https://www.gsmarena.com/'
brands = []
#print("here")
brandurl = 'https://www.gsmarena.com/makers.php3'

brandrespone = requests.get(brandurl)
brandsoup = BeautifulSoup(brandrespone.content, 'html5lib') 
tablelist = brandsoup.find_all('table')[0]
#print (table)
tablehref = tablelist.find_all('a')
#print(tablehref)

for a in tablehref:
    #print(a.attrs["href"])
    temp = a.attrs["href"]
    brands.append(temp)
#print(brands)

with open("Dataset.txt","w",encoding="utf-8") as fileobj:
    for brand in brands:
        specbrandurl = baseurl + brand
        #print(specbrandurl)
        specbrandrespone = requests.get(specbrandurl)
        #print(specbrandrespone.content)
        specbrandsoup = BeautifulSoup(specbrandrespone.content, 'html5lib')
        #print(specbrandsoup)
        if specbrandsoup is None:
           continue
        specbrandtbl = specbrandsoup.find_all("img")
        #print(specbrandtbl)

        for i in specbrandtbl:
            if i.has_attr('title'):
                temp = i.attrs['title']
                #print(type(temp))
                #if (len(temp) > 250):
                temp1 = temp.replace(".",",",2)
                temp2 = temp1.replace("Features","")
                temp3 = temp2
                if(len(temp3.split(",")) >= 10):
                    fileobj.write(temp2)
                    fileobj.write("\n")
                #if specbrandtbl is None:
                #   continue
                #temp = specbrandtbl.find("title")
                #print(temp)
    #fileobj.close()