import re
import conn
import parsing
from bs4 import BeautifulSoup
import site_parsing



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
