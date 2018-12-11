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
            WHERE Players.Nationality='France'
            ORDER BY Players.'Market Value' DESC
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list), 384)
        self.assertEqual(result_list[2][2], 'Paul Pogba')

        conn.close()

unittest.main()