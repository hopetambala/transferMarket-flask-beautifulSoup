import csv
import sqlite3 as sqlite
from sqlite3 import Error

def create_soccer_db():
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite.connect('soccerDB.sqlite')
        print(sqlite.version)
    except Error as e:
        print(e)

    cur = conn.cursor()


    '''
    Drop Tables
    '''
    statement = '''
        DROP TABLE IF EXISTS 'Leagues';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Players';
    '''
    cur.execute(statement)


    '''
    Create Tables
    '''

    statement = '''
        CREATE TABLE 'Leagues' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Name' TEXT NOT NULL,
            'NumberOfTeams' TEXT NOT NULL,
            'NumberOfPlayers' TEXT NOT NULL
        );
    '''
    cur.execute(statement)

    statement = '''
        CREATE TABLE 'Players' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'JerseyNumber' INTEGER NOT NULL,
            'Name' TEXT NOT NULL,
            'Position' TEXT NOT NULL,
            'Birthday' TEXT NOT NULL,
            'Nationality' TEXT NOT NULL,
            'Team' TEXT NOT NULL
        );
    '''
    
    cur.execute(statement)


    conn.close()

def populate_soccer_db():
    # Connect to big10 database
    conn = sqlite.connect('soccerDB.sqlite')
    cur = conn.cursor()

    with open('leagues.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
                insertion = (None, row[0], row[1], row[2])
                statement = 'INSERT INTO "Leagues" '
                statement += 'VALUES (?, ?, ?, ?)'
                cur.execute(statement, insertion)
    
    with open('players.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
                insertion = (None, row[0], row[1], row[2], row[3],row[4],row[5])
                statement = 'INSERT INTO "Players" '
                statement += 'VALUES (?, ?, ?, ?, ?, ?,?)'
                cur.execute(statement, insertion)
    # Close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_soccer_db()
    print("Created soccer Database")
    populate_soccer_db()
    print("Populated soccer Database")