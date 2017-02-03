# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com',80))

# mysock.send('GET http://py4inf.com/code/romeo.txt HTTP/1.0\n\n')

# while True:
    # data = mysock.recv(512)
    # if ( len(data) < 1) :
        # break
    # print data
# mysock.close()   

# import urllib
# fhand = urllib.urlopen('http://ip-api.com/json/208.80.152.201')
# for line in fhand:
    # print line.strip()

import csv  
import urllib
numlist = list()
numlist2 = list()   
dhand = open('ips.csv')
for line in dhand:
    fhand = urllib.urlopen('http://ip-api.com/json/'+line)
    for ip in fhand:
        piece = ip.split(',')
        numlist.append(line.strip())
        numlist.append(piece[1])
        numlist.append(piece[2])
        
# Split the list at nth point
# n = 3
# endlist = [[] for _ in range(n)]
# for index, item in enumerate(numlist):
    # endlist[index % n].append(item)
# length = len(endlist[0])

# Split the list at even points
n = 3
numlist2 = [numlist[i:i+n] for i in range(0, len(numlist), n)]


with open("output2345.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(numlist2)
    
