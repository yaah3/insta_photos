import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import selenium.webdriver as webdriver
url = input("PLEASE ENTER VALID URL: ")
driver = webdriver.Chrome()
try:
	driver.get(url)
except:
	print("url not found")
	exit(1)
soup = BeautifulSoup(driver.page_source,features="lxml")
f=open("links","a+")
images=soup.find_all('img')
k=0
for image in images:
	k=k+1
	print(image['src'])
	f.write(image['src'] + "\n")
f.close()
print('Number of pictures that will be downloaded : ' + str(k))
f=open("links","r")
k=1
for x in f:
	try:
		urllib.request.urlretrieve(x,str(k)+'.jpg')
	except:
		k-=1
	k=k+1
f.close()
