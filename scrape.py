# import csv
# allurls = csv.reader(open('home24.csv') )
# rows=list(allurls)

# import requests 
# from bs4 import BeautifulSoup
# for i in rows:
    # site = urlopen(url)   
        # soup = BeautifulSoup(site, "lxml")
        # for item in soup.find_all("div", {"class": "vm-product-descr-container-1"}):
            # print item.text

# soup.find_all('b')
# This code finds all the 'b' tags in the document (you can replace b with any tag you want to find)

# soup.find_all(re.compile("^b"))
# This code finds all the tags whose names start with the letter "b"

# soup.find_all("title")
# soup.find_all("p", "title")
# soup.find_all("a")
# soup.find_all(id="link2")
			
import csv  
from datetime import datetime	
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

with open('home24.csv') as inf:
    urls = (line.strip() for line in inf)
    for url in urls:
        site = urlopen(url)   
        soup = BeautifulSoup(site, "html.parser")
        for item in soup.find('span', attrs={'class':'product-details__key-information__item__option'}) :
            # print(item)
            with open('output.csv', 'a', newline='') as csv_file:  
                writer = csv.writer(csv_file)
                writer.writerow([url,item, datetime.now()])