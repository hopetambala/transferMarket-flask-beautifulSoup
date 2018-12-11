import unittest
import json
import requests
import csv

TEAMJSON = 'teams.json'
LEAGUEJSON = 'leagues.json'

PLAYERSCSV = 'players.csv'
TEAMSCSV = 'teams.csv'
LEAGUESCSV = 'leagues.csv'

class TestCaches(unittest.TestCase):

    def test_team_json(self):
        with open(TEAMJSON) as json_data:
            c = json.load(json_data)

        for obj in c:
            self.assertIn('www.transfermarkt.com', obj)
        self.assertIn('new-england-revolution',str(c))
        self.assertIn('arsenal',str(c))
        self.assertIn('barcelona',str(c))
    def test_leagues_json(self):
        with open(LEAGUEJSON) as json_data:
            c = json.load(json_data)

        for obj in c:
            self.assertIn('www.transfermarkt.com', obj)
        self.assertIn('premier-league',str(c))
        self.assertIn('bundesliga',str(c))
        
class testCSVS(unittest.TestCase):
    def test_leagues(self):
        with open(LEAGUESCSV) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.assertTrue(type(row[0]),type(0))
                self.assertTrue(type(row[1]),type(""))

    def test_players(self):
        with open(PLAYERSCSV) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.assertTrue(type(row[0]),type(0))
                self.assertTrue(type(row[1]),type(""))
    
    def test_teams(self):
        with open(TEAMSCSV) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.assertTrue(type(row[0]),type(1))


unittest.main()