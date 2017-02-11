import urllib
x = 0
z = 3
y = 12
numlist = list()
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')

for tag in tags:
    x = x + 1
        # print x 
    if x == z:
        print tag.get('href', None)
        z = z + 3
        if z < y:
            continue
        else:
            break
            
            

    