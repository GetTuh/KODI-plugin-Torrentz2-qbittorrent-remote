from qbittorrent import *
import re
import json

try:
	qb = Client('http://192.168.0.101:8080')
	qb.login('admin', 'q1w2e3')
except:
	print("error kurwa")



def add_torrent(magnet):
	qb.download_from_link(magnet)
	tor_hash = magnet_to_hash(magnet)
	qb.toggle_sequential_download(tor_hash)

def magnet_to_hash(magnet): #Searches for torrent using magnet, returns hash
	magnet_url=magnet.lower()
	magnet_url=re.match(".*?&dn=", magnet_url).group(0)
	alltorrents = qb.torrents()
	tor_hash=""
	for torrent in alltorrents:
		torrent_magnet = torrent['magnet_uri'].lower()
		torrent_magnet = re.match(".*?&dn=", torrent_magnet).group(0)
		if(torrent_magnet==magnet_url):
			tor_hash=torrent['hash']
	return tor_hash

# add_torrent(magnet)

def delete_torrent_pernament(magnet):
	tor_hash = magnet_to_hash(magnet)
	qb.delete_permanently(tor_hash)

# delete_torrent_pernament(magnet)

