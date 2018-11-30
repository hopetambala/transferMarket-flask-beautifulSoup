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
    baseurl = 'https://www.transfermarkt.com/'

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

def getTeamsAndPlayers():

    leagues = [
        ('premierleague','premier-league/startseite/wettbewerb/GB1/saison_id/2018'),
        ('bundesliga','bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2018'),
        ('laliga','laliga/startseite/wettbewerb/ES1/plus/?saison_id=2018'),
        ('ligue1','ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2018'),
        ('serieA',"serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2018"),
        ('mls','major-league-soccer/startseite/wettbewerb/MLS1/plus/?saison_id=2017')

    ]

    for league in leagues:
        stats_soup = getWhoScoredDataSoup(league[0],league[1])

        #print(stats_soup.prettify())

        #gets me the table
        divs = stats_soup.find("div", id="yw1").find('tbody')

        rows = divs.find_all('tr')


        for row in rows:
            #Club Name
            img = row.find('img',alt=True)
            print(img['alt'])

            row_of_a= row.find_all('a', href = True,class_='vereinprofil_tooltip')
            first_element = row_of_a[0]
            
            urlExtension = first_element.get('href')
            print(urlExtension)

getTeamsAndPlayers()