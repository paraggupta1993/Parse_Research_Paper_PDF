import requests
import sys

INFINITE = 99999999

potential_second_heading =  [
'keyword',
'keywords',
'introduction',
'1 introduction',
'1.introduction',
'1. introduction',
'1.  introduction',
'1) introduction',
'Categories',
'General Term',
'Index Term',
'Literature Review'
]

def getIndex(lowercontent, word):
	try:
		return lowercontent.index(word)
	except ValueError:
		return INFINITE

def parseResponse(response):
	#print response.keys()
	#print response['document'][0].keys()
	#print response['document'][0]['content']
	content = response['document'][0]['content']
	lowercontent = content.lower()

	#finding index of headings in lowercase

	abstracti = getIndex(lowercontent, "abstract")
	lastpos = INFINITE
	for heading in potential_second_heading:
		lastpos = min(lastpos, getIndex(lowercontent, heading.lower()))

	if abstracti != INFINITE:
		print content[abstracti:lastpos][8:]
	else:
		print 'Unable to extract Abstract'

def main():
	filename = sys.argv[1]
	apikey="7ed85924-1cdd-46ea-9b6d-a9c309061335"
	url =  "https://api.idolondemand.com/1/api/sync/extracttext/v1"

	data = {}
	data["apikey"] = apikey
	r = requests.post(url,data=data, files={'file':open(filename,'rb')})
	parseResponse(r.json())

if __name__ == '__main__':
	main()
