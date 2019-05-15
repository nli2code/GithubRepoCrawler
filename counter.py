import json

with open("urlList.json") as f:
    arr = json.load(f)
    print arr[0]
    print len(arr) 
