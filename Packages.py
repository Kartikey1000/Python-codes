'''import cowsay
import sys
if len(sys.argv)==2:
    cowsay.trex("hello, "+sys.argv[1])#cow can also be used 
'''
#APIs
import requests
import sys
import json

if len(sys.argv) !=2:
    sys.exit()

response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])

o= response.json()
for result in o["results"]:
    print(result["trackName"])

