import json
import requests
from requests.auth import HTTPBasicAuth

with open('config.json', 'r') as f:
	data = json.load(f)
	query = data['query']
	auth_id = data['auth_id']
	auth_pwd = data['auth_pwd']

def getJsonFromUrl(url) :
	results = requests.get(url,auth = HTTPBasicAuth(auth_id,auth_pwd))
	data = json.loads(results.content);
	return data

def getSubUrlList(url):
	subUrlList = []
	try:
		queryResults = getJsonFromUrl(url)
	except Exception as e:
		queryResults = None
		print e
	if(queryResults == None or not queryResults.has_key('items')):
		return []

	for item in queryResults['items']:
		subUrlList.append(item['html_url'])
	return subUrlList

def getUrlList(query):
	queryUrl = 'https://api.github.com/search/repositories?' + query
	try:
		queryResults = getJsonFromUrl(queryUrl)
	except Exception as e:
		queryResults = None
		print e
	if(queryResults == None):
		return

	total_count = queryResults['total_count']
	print total_count
	if(total_count>1000):
		total_count = 1000
	total_page = (total_count + 29)/30

	urlList = []
	for pageNum in xrange(1,total_page+1):
		subUrlList = getSubUrlList(queryUrl + '&page=' + str(pageNum))
		urlList.extend(subUrlList)
		print pageNum
	return urlList

if __name__ == '__main__':
	urlList = getUrlList(query)
	with open('urlList.json', 'w') as file:
		json.dump(urlList,file)
	print urlList




