# SG Telegram Channels Scraper

How to scrape:

In your shell run: 
* `python scrape_channels.py --file <input filename>` where filename is a file of telegram channel urls
    * masterlist of URLs is kept in `url_masterlist.txt`
* or, for a single channel `python scrape_channels.py <url-to-channel>`

As an example running the `sample_list.txt` file creates `scrape_channels_210805.csv` in the data directory
* export filename convention is `scrape_<input filename>_<date>.csv`

## Directory description
Scripts:
* `scrape_channels.py`: scraper for telegram channel information
    * [ ] TODO: multiprocessing to make it faster 

Data Files:
inputs: 
* `sample_list.txt`: a sample of 10 urls
* `url_masterlist.txt`: our database of telegram channel urls

outputs:
* see `data/` for scraped outputs
* [ ] TODO: master sheet for all scraped info, to be updated automatically with every new scrape run
    
Notebooks (`/notebooks`):
* `exploration.ipynb`: poking around, used code in here to develop the `scrape_channels` script
