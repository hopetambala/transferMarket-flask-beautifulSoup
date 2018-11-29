import requests
import json
from bs4 import BeautifulSoup



def loadJson(name):
    CACHE_FNAME = str(name) + '.json'
    try:
        cache_file = open(CACHE_FNAME, 'r')
        cache_contents = cache_file.read()
        CACHE_DICTION = json.loads(cache_contents)
        cache_file.close()
    except:
        CACHE_DICTION = {}
    return CACHE_DICTION

def getWhoScoredDataSoup(cacheName, specifier):
    #baseurl = 'https://www.whoscored.com/'
    baseurl = 'https://www.transfermarkt.com/'

    #page_url = baseurl + "/Statistics"
    page_url = baseurl + str(specifier)
    header = {'User-Agent': 'hope'}

    CACHE_DICTION = loadJson(str(cacheName))

    unique_ident = page_url

    if unique_ident in CACHE_DICTION:
        page_text = CACHE_DICTION[unique_ident]
    else:
        page_text = requests.get(page_url,headers=header).text #original
        CACHE_DICTION[unique_ident] = page_text
        dumped_json_cache = json.dumps(CACHE_DICTION,indent=4)
        fw = open(str(cacheName)+'.json',"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file


    page_soup = BeautifulSoup(page_text, 'html.parser')
    return page_soup

def getStatistics():
    stats_soup = getWhoScoredDataSoup('premierleague',"premier-league/startseite/wettbewerb/GB1/saison_id/2018")
    #print(stats_soup.prettify())


    #name_div = stats_soup.find_all("a",  class_="team-link")


    #gets me something statistics-team-table-detailed
    divs = stats_soup.find("div", id="yw1").find('tbody')

    rows = divs.find_all('tr')


    for row in rows:
        #Club Name
        img = row.find('img',alt=True)
        print(img['alt'])

        


    # The different tables
    '''
    tableNames = ['summary', 'defensive', 'offensive', 'passing']
    table = soup.find("div", {"id": "statistics-table-" + tableName }).find("tbody", {"id": "player-table-statistics-body"})
    '''

    '''
    for name in name_div:
        print(name)
    '''
getStatistics()