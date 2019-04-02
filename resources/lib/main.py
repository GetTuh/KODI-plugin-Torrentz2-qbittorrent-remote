import re
import conn
import parsing
from bs4 import BeautifulSoup
import site_parsing
item_searched = "https://torrentz2.eu/search?f=one"


def get_items(item_searched):
    data = ()
    raw_html = conn.simple_get(item_searched)
    soup = BeautifulSoup(raw_html, 'html.parser')
    adblock = 2
    for dl in soup.find_all("dl"):  # parsowanie wynikow
        if adblock != 0:  # dwa pierwsze wyniki to zawsze reklamy
            adblock -= 1
        else:
            data += parsing.parse_names(dl)
    return data

getmagnet = "https://torrentz2.eu/e2e457b2e77128cd20fafd0837bbdb9a4d543578";


def get_torrent_site(addresses):
    try:
        data = ()
        raw_html = conn.simple_get(addresses)
        soup = BeautifulSoup(raw_html, 'html.parser')
        adblock = 1
        for dl in soup.find_all('a', attrs={"href": re.compile('http')}):  # parsowanie wynikow
            if adblock != 0:  # dwa pierwsze wyniki to zawsze reklamy
                adblock -= 1
            else:
                print(dl)

    except TypeError:
        pass

if __name__ == "__main__":
    searched_sites = get_items(item_searched)

    get_torrent_site(getmagnet)
