# Flask - TransferMarkt 
Scrape and Crawl International Football Information into a SQLite Database


## Project Layout
├── data                      # Folder for Generated JSON Cache, CSVs, and SQLite Database
├── scripts                   # Crawling/Scraping Script, Database Importer Script
├── static                    # Static Files
├── templates                 # HTML Templates
├── app.py                    # Main Application
├── queries.py                # SQLite Database Queries
├── Procfile                  # Heroku File to Run App on Web
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

Run main Flask application
```
python3 app.py
```


#Heroku Details
https://transfrmarkt-flask.herokuapp.com/
https://git.heroku.com/transfrmarkt-flask.git


