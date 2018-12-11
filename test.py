import unittest
from app import *
from queries import *

DBNAME = 'soccerDB.sqlite'

class TestDatabase(unittest.TestCase):

    def test_players_table(self):
        conn = sqlite.connect(DBNAME)
        cur = conn.cursor()

        sql = 'SELECT Name from Players'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('Lionel Messi',), result_list)
        self.assertEqual(len(result_list), 3300)

        sql = '''
            SELECT * from Players
            WHERE Players.Nationality='France' AND Players.'Market Value'
            ORDER BY Players.'Market Value' DESC
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list), 383)
        self.assertEqual(result_list[2][2], 'Paul Pogba')

        conn.close()
    def test_teams_table(self):
        conn = sqlite.connect(DBNAME)
        cur = conn.cursor()

        sql = '''
            SELECT Name, NumberofForeigners From Teams
            WHERE Teams.NumberofForeigners > 20
            ORDER BY Teams.NumberofForeigners DESC;'''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(result_list[1][0], 'Cardiff City')
        self.assertEqual(len(result_list), 15)

        sql = '''
            SELECT Players.Name, Players.Team, Players.'Market Value',Teams.TotalMarketValue from Players
            JOIN Teams
                ON Teams.Name=Players.Team
            WHERE Players.'Market Value'
            ORDER BY Players.'Market Value' DESC
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list), 3293)
        self.assertEqual(result_list[7][3], 1230000000)

        conn.close()

unittest.main()