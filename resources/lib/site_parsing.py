import re
from bs4 import BeautifulSoup
import conn

def torrent_sites(site):
    sources = (site.find('a', href=True)['href'])
    print(sources)



