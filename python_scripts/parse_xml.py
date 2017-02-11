import urllib
import xml.etree.ElementTree as ET
k = 0
j = 0
numlist = list()

url = 'http://python-data.dr-chuck.net/comments_42.xml'

html = urllib.urlopen(url).read()
stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment')
for item in lst:
	tags = item.find('count').text
	j = int(tags)
	k = j + k
	print k
	# for tag in tags:
		# print tag
		# j = int(tag)
		# print j
		# k = j + k
		# print k
    