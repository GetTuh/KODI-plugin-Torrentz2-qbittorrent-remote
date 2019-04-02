from bs4 import BeautifulSoup
import re
import conn
import parsing

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

def addresses():
    address_list = [x for x in searched_sites ]
    print(address_list)

searched_sites = get_items(item_searched)
addresses()

