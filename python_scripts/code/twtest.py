import urllib
from twurl import augment

print '* Calling Twitter...'
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {'screen_name': 'ygdimitrov', 'count': '1'} )
print url
connection = urllib.urlopen(url)
data = connection.read()
print data
headers = connection.info().dict
print headers
