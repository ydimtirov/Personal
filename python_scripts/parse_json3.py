import json
import urllib
x = 0
# url = "http://python-data.dr-chuck.net/comments_42.json"
url = "http://ip-api.com/json/208.80.152.201"

# [
  # { "id" : "001",
    # "x" : "2",
    # "name" : "Chuck"
  # } ,
  # { "id" : "009",
    # "x" : "7",
    # "name" : "Chuck"
  # } 
# ]'''

html = urllib.urlopen(url)
data = html.read()
info = json.loads(data)
# print json.dumps(info, indent=4)

print info['city']
print info['country']

# for line in info['comments']:
	# print line ['count']
	# j = int(line ['count'])
	# print j
	# x = j + x
# print x

# for line in info['comments']
    # print 'Name', line['count']
