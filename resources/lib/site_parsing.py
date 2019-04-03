import re
from bs4 import BeautifulSoup
import conn
import time
def link_to_magnet(site):
    raw_html = conn.simple_get(site)
    soup = BeautifulSoup(raw_html, 'html.parser')
    all_links = soup.findAll("div", {"class": "downlinks"})
    all_links = all_links[0].findAll("a")
    adblock=0
    for siteLink in all_links:
    	if(adblock==0):			#pierwszy wynik to reklama wiec go omijam
    		adblock+=1
    	else:
    		siteLink=siteLink.get('href')
    		print("trying " + siteLink)
    		magnet = siteLink_to_magnet(siteLink)
    		if(magnet!=None):
    			return(magnet)
    		print("No magnet found")


def siteLink_to_magnet(siteLink):
    raw_html = conn.simple_get(siteLink)
    try:
	    soup = BeautifulSoup(raw_html, 'html.parser')
	    mag_re=re.compile("href=\"magnet:\?")
	    magnet = soup.findAll('a')
	    for a in magnet:
	    	if re.findall("href=\"magnet:\?",str(a.encode('utf-8'))):
	    		return(a.get('href'))
    except:
    	return None

# print(siteLink_to_magnet("https://1337x.to/torrent/3223403/Solo-A-Star-Wars-Story-2018-BluRay-1080p-YTS-YIFY/"))

print(link_to_magnet("https://torrentz2.eu/e2e457b2e77128cd20fafd0837bbdb9a4d543578"))