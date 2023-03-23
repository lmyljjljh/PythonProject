import requests
import pprint
t1 = requests.get('http://api.github.com/events')
pprint.pprint(t1.text)