import requests
import json
from bs4 import BeautifulSoup

BASEURL = 'https://www.transfermarkt.com/'

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
    baseurl = BASEURL

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
    #Leage Information loop
    for league in leagues:
        #League Soup
        #stats_soup = getWhoScoredDataSoup(league[0],league[1])
        stats_soup = getWhoScoredDataSoup('leagues',league[1])
        #gets me the table
        divs = stats_soup.find("div", id="yw1").find('tbody')

        rows = divs.find_all('tr')

        #Team Information Loop
        for row in rows:
            #Club Name
            img = row.find('img',alt=True)
            club_name = img['alt']
            

            #Club URL
            row_of_a= row.find_all('a', href = True,class_='vereinprofil_tooltip')
            first_element = row_of_a[0]
            
            urlExtension = first_element.get('href')
            clubs_soup = getWhoScoredDataSoup('teams',urlExtension[1:]) #removes extra comma
        
            team_divs = clubs_soup.find("div", id="yw1").find('tbody')

            team_rows_odd = team_divs.find_all('tr',class_='odd')
            team_rows_even = team_divs.find_all('tr',class_='even')
            team_rows = team_rows_even + team_rows_odd
            
            #Player Information Loop
            for row in team_rows:
                #print(row.find("td")) //prints some goodies
                
                
                #Player Number
                print(row.find('div',class_='rn_nummer').text)
                
                #Player Name
                print(row.find('td',class_='hide').text)
                
                #Position
                all_trs = row.find('table',class_='inline-table').find_all('tr')
                position = all_trs[1].text
                print(position)
                
                #Birthday
                print(row.find_all('td',class_='zentriert')[1].text) 
                
                #Nationality
                print(row.find('img',class_='flaggenrahmen')['alt'])

                #Club
                print(club_name)

                
                #print(row.prettify())
                
                
                
                print('')

                #print(row.prettify())
                
            
            #print(BASEURL[:29] + urlExtension)

getTeamsAndPlayers()