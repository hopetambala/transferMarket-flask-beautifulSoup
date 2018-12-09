import sqlite3 as sqlite
#from sqlite3 import Error


#Teams In Descending Order Based on Market Value
def get_teams():
    statement = '''
        SELECT * from Teams
        ORDER BY Teams.TotalMarketValue DESC; 
        '''

    conn = sqlite.connect('soccerDB.sqlite')
    cur = conn.cursor()
    cur.execute(statement)

    rows = cur.fetchall()
    return(rows)

def get_players():
    statement = '''
        SELECT * from Players
        ORDER BY Players.'Market Value' DESC;
    '''

    conn = sqlite.connect('soccerDB.sqlite')
    cur = conn.cursor()
    cur.execute(statement)

    rows = cur.fetchall()
    return(rows)

def count_player_positions():
    statement = '''
        SELECT Players.Position, COUNT(*) AS `CountOfPosition`, AVG(Players.'Market Value') as  `Average`
        FROM Players
        GROUP BY Position
    '''

    conn = sqlite.connect('soccerDB.sqlite')
    cur = conn.cursor()
    cur.execute(statement)

    rows = cur.fetchall()
    return(rows)