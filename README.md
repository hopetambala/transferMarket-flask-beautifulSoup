# Flask - TransferMarkt 
Scrape and Crawl International Football Information into a SQLite Database


## Description
This application scrapes and crawls through multiple pages of this data source: [TransferMarket.com](https://www.transfermarkt.com/), a soccer website that displays the market value of multiple soccer teams and players.


## Project Layout
    ├── data                      # Folder for Generated JSON Cache, CSVs, and SQLite Database
    ├── scripts                   # Crawling/Scraping Script, Database Importer Script
    ├── static                    # Static Files
    ├── templates                 # HTML Templates
    ├── app.py                    # Main Application
    ├── queries.py                # SQLite Database Queries
    ├── Procfile                  # Heroku File to Run App on Web
    ├── test.py                   # Unit Testing
    └── README.md

## Getting Started
Run scraper.py to scrape websites and create CSVs
```
cd data
python3 ../scripts/scraper.py
```

Run import.py to import CSVs into SQLite database
```
cd data
python3 ../scripts/importer.py
```

Move the created database from data/ to the main project folder
```
cd <Main Project Folder>
mv data/soccerDB.sqlite ./
```
or
```
cd data
mv soccerDB.sqlite ../
```

Run main Flask application
```
python3 app.py
```

## Testing
To Test Database (Make sure you're in the virtual environmenta)
```
cd <Main Project Folder>
python3 test.py
```

To Test Data Sources

```
cd data/
python3 test.py
```


#Heroku Details
    https://transfrmarkt-flask.herokuapp.com/
    https://git.heroku.com/transfrmarkt-flask.git


