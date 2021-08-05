# SG Telegram Channels Scraper

How to scrape:

In your shell (on Mac, that's Terminal) run: 
* `python scrape_channels.py --file <filename>` where filename is a file of telegram channel urls (see `sample_list.txt` -- yes, 1 url is broken)
* or, for a single channel `python scrape_channels.py <url-to-channel>`

As an example running the `sample_list.txt` file creates `scrape_channels_210805.csv` in the data directory

## Directory description
Scripts:
* `scrape_channels.py`: scraper for telegram channel information
    
Notebooks:
* `exploration.ipynb`: poking around, used code in here to develop the scrape_channels script
