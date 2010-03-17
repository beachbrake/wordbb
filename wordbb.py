
import httplib

import simplejson as json

import pprint

import sys

if (len(sys.argv) == 1):
    print "Please specify a word."
    sys.exit(0)

conn = httplib.HTTPConnection("api.wordnik.com")

params = {}
headers = {"api_key": "Your key here"}

conn.request("GET", "/api/word.json/" + sys.argv[1] + "/definitions", params, headers)

r1 = conn.getresponse()
#print r1.status, r1.reason

data1 = r1.read()

words = json.loads(data1)

i = 0

j = 1

while i < len(words):
    if "headword" in words[i]:
        if "text" in words[i]:
            print "------------------------------------------------------------"

            print str(j) + ") " + words[i]["headword"]
            j = j + 1
            print "\t" + words[i]["text"]


    i = i + 1

conn.close()


