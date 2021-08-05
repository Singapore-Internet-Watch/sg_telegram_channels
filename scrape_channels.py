"""Scrapes Telegram channel information and outputs a csv file.

Usage:
    scrape_channels.py CHANNEL_URL
    scrape_channels.py --file FILE
    
Options:
    --file  Pass a file of channel names to scrape.
"""

from docopt import docopt
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date


def channel_verified(title_html_obj):
    if title_html_obj.i:
        return True
    return False

def channel_subs(subs_html_obj):
    subs_string = subs_html_obj.text
    subs_int = ''
    if 'subscribers' in subs_string:
        subs_int = int(subs_string.replace('subscribers', '').replace(' ', ''))
    elif 'online' in subs_string:
        subs_int = int(subs_string.split(',')[0].replace(' members', '').replace(' ', ''))
    return subs_int

def channel_desc(desc_html_obj):
    if desc_html_obj:
        return desc_html_obj.text.strip()
    else:
        return ''
    

if __name__ == '__main__':
    args = docopt(__doc__)
    urls = []
    tele_channels = pd.DataFrame(columns=['channel', 'verified', 'description', 'subscribers', 'url', 'date_accessed'])
    date_scraping = date.today().strftime('%y%m%d')

    
    if args['--file']:
        with open(args.get('FILE')) as f: 
            urls = f.read().splitlines()
    else:
        urls = [args.get('CHANNEL_URL')]

    error_urls = []
    for i in range(len(urls)):
        print(f'Scraping channel {i+1} of {len(urls)}')
        try:
            tele_url = urls[i]
            r = requests.get(tele_url)
            soup = BeautifulSoup(r.content, 'html.parser')

            channel_info = {'channel': soup.find(class_='tgme_page_title').text.strip(),
                       'verified': channel_verified(soup.find(class_='tgme_page_title')),
                       'description': channel_desc(soup.find(class_='tgme_page_description')),
                       'subscribers': channel_subs(soup.find(class_='tgme_page_extra')),
                       'url': tele_url,
                       'date_accessed': date_scraping}

            tele_channels = tele_channels.append(channel_info, ignore_index=True)
        except:
            error_urls.append(urls[i])
            continue
        
    export_filename = f'data/scrape_channels_{date_scraping}.csv'
    tele_channels.to_csv(export_filename, index=False)
    print(f'Exported scraped data to {export_filename}')
    if len(error_urls)>0:
        print(f'Could not scrape urls: {error_urls}')
