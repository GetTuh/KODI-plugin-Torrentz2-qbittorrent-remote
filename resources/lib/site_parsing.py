import re
from bs4 import BeautifulSoup
import conn

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
    		print(siteLink.get('href'))

def siteLink_to_magnet(siteLink):
	pass



link_to_magnet("https://torrentz2.eu/e2e457b2e77128cd20fafd0837bbdb9a4d543578")