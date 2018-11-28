import requests
import json
from bs4 import BeautifulSoup


CACHE_FNAME = 'cacheData.json'
def loadJson(CACHE_FNAME):
    try:
        cache_file = open(CACHE_FNAME, 'r')
        cache_contents = cache_file.read()
        CACHE_DICTION = json.loads(cache_contents)
        cache_file.close()
    except:
        CACHE_DICTION = {}
    return CACHE_DICTION

def getWhoScoredData():
    baseurl = 'https://www.whoscored.com/Statistics'

    CACHE_DICTION = loadJson(CACHE_FNAME)

    unique_ident = baseurl

    if unique_ident in CACHE_DICTION:
        page_text = CACHE_DICTION[unique_ident]
    else:
        page_text = requests.get(baseurl).text #original
        CACHE_DICTION[unique_ident] = page_text
        dumped_json_cache = json.dumps(CACHE_DICTION,indent=4)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file

        page_soup = BeautifulSoup(page_text, 'html.parser')

        return page_soup
    
whoScoredSoup = getWhoScoredData()