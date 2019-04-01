from bs4 import BeautifulSoup
import conn
import re
import parsing

item_searched = "https://torrentz2.eu/search?f=one"



def get_names_and_sources(item_searched):
	tuple=()
	raw_html = conn.simple_get(item_searched)
	soup = BeautifulSoup(raw_html, 'html.parser')
	adblock = 2
	for dl in soup.find_all("dt"):  # parsowanie wynikow
		if adblock != 0:  # dwa pierwsze wyniki to zawsze reklamy
			adblock -= 1
		else:
			tuple+=parsing.parse_names(dl)
	return(tuple)


# source = "\/6e057822dec074b5a0b792f5dc99b1697822806b"
# magnet = prasing.source_to_magnet(source)
get_names_and_sources(item_searched)
