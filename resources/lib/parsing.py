import re
import site_parsing
from bs4 import BeautifulSoup

def parse_names(html):
    names = html.find("a").get_text().encode("utf-8")
    names = str(names)
    names = re.sub(r'b\'', '', names)
    names = re.sub(r'\'', '', names)
    sources = (html.find('a', href=True)['href'])
    return (names, sources)


def source_to_magnet(source):
    raw_html = conn.simple_get(source)
    soup = BeautifulSoup(raw_html, 'html.parser')
    for link in soup.body.findAll(text='monova.org'):
    	pass