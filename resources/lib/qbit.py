from qbittorrent import *
import re
import json
magnet="magnet:?xt=urn:btih:E2E457B2E77128CD20FAFD0837BBDB9A4D543578&dn=Solo+A+Star+Wars+Story+%282018%29+%5BBluRay%5D+%281080p%29&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969"
try:
	qb = Client('http://192.168.0.101:8080')
except:
	print("error kurwa")

qb.login('admin', 'q1w2e3')

def add_torrent(magnet):
	qb.download_from_link(magnet)
	magnet_url=magnet.lower()
	magnet_url=re.match(".*?&dn=", magnet_url).group(0)
	alltorrents = qb.torrents()
	tor_hash=""
	for torrent in alltorrents:
		torrent_magnet = torrent['magnet_uri'].lower()
		torrent_magnet = re.match(".*?&dn=", torrent_magnet).group(0)
		if(torrent_magnet==magnet_url):
			tor_hash=torrent['hash']
	qb.toggle_sequential_download(tor_hash)

add_torrent(magnet)