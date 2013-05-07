#Retrieves 15 of the most recent tweets about 'underpants'

import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=underpants")


pyresponse = json.load(response)

#print pyresponse["results"]

results = pyresponse["results"]

for i in range(15):
    print results[i]["text"]

