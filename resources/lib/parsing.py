import re
import site_parsing
from bs4 import BeautifulSoup

def parse_names(html):
    names = html.find("a").get_text().encode("utf-8")
    names = str(names)
    names = re.sub(r'b\'', '', names)
    names = re.sub(r'\'', '', names)
    sources = (html.find('a', href=True)['href'])
    x=0
    for link in html.find_all('span'):
        if(x%4==0):
            seeds=link.get_text()
        if(x%4==1):
            time=link.get_text()
        if(x%4==2):
            size=link.get_text()
        if(x%4==3):
            peers=link.get_text()
        x+=1
    return (names, sources, time,size,seeds,peers)


def source_to_magnet(source):
    raw_html = conn.simple_get(source)
    soup = BeautifulSoup(raw_html, 'html.parser')
    for link in soup.body.findAll(text='monova.org'):
    	pass