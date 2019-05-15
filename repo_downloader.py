import os
import json

if __name__ == '__main__':
	os.system('mkdir repo')
	with open('urlList.json', 'r') as file:
		urlList = json.load(file)
	for url in urlList:
		print url
		os.system('git clone --depth=1 ' + url + ' ./repo/' + url.split('/')[-2] + '/' + url.split('/')[-1])