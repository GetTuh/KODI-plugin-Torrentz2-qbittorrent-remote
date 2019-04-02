import re
from bs4 import BeautifulSoup
import conn
link_to_site = "https://torrentz2.eu"

def parse_names(html):
    names = html.find("a").get_text().encode("utf-8")
    names = str(names)
    names = re.sub(r'b\'', '', names)
    names = re.sub(r'\'', '', names)
    sources = link_to_site + (html.find('a', href=True)['href'])
    x = 0
    for link in html.find_all('span'):
        if (x % 4 == 0):
            seeds = link.get_text()
        if (x % 4 == 1):
            time = link.get_text()
        if (x % 4 == 2):
            size = link.get_text()
        if (x % 4 == 3):
            peers = link.get_text()
        x += 1
    return (names, sources, time, size, seeds, peers)



def get_pirate_site(address):
    data = ()
    raw_html = conn.simple_get(address)
    soup = BeautifulSoup(raw_html, 'html.parser')
    adblock = 2
    for dl in soup.find_all("dl"):  # parsowanie wynikow
        if adblock != 0:  # dwa pierwsze wyniki to zawsze reklamy
            adblock -= 1
        else:
            data += parsing.parse_names(dl)
    return data

