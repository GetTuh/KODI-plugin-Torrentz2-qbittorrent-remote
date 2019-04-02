import re
from bs4 import BeautifulSoup
import conn

def magnet(site):
    try:
        raw_html = conn.simple_get(site)
        soup = BeautifulSoup(raw_html, 'html.parser')

        for dl in soup.find_all('a', attrs={"href": re.compile('magnet')}):  # parsowanie wynikow
            torrent =re.search('magnet\w\S*\w',str(dl))
            torrent = torrent.group()
            print(torrent)
    except (TypeError, AttributeError):
        pass


