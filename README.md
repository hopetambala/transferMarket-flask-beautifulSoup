# Flask - TransferMarkt 
Scrape and Crawl International Football Information into a SQLite Database


## Project Layout
├── data                      # Folder for Generated JSON Cache, CSVs, and SQLite Database
├── scripts                   # Crawling/Scraping Script, Database Importer Script
├── static                    # Static Files
├── templates                 # HTML Templates
├── app.py                    # Main Application
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


