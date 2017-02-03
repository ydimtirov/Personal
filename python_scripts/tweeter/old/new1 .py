import oauth2 as oauth
import json

CONSUMER_KEY = "oPdBkVM6HnzqqlvIdiif6kQhM"
CONSUMER_SECRET = "q6K8fzjDtOh0DWPI4wm2ZGjsGlqzhVOFLXw9gifeJAebWtyqw0"
ACCESS_KEY = "1171294657-HfIBEigweXCuOrJzGTLMdWmOezKFAoEggHsZZf3"
ACCESS_SECRET = "9iDm6T9L3ij80MArcM7zOofuUqoQ01ayYQVBXkfLZIDB7"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']