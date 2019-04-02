from qbittorrent import *
import json
magnet="magnet:?xt=urn:btih:E2E457B2E77128CD20FAFD0837BBDB9A4D543578&dn=Solo+A+Star+Wars+Story+%282018%29+%5BBluRay%5D+%281080p%29&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969"
try:
	qb = Client('http://192.168.0.101:8080')
except:
	print("error kurwa")

qb.login('admin', 'q1w2e3')

qb.download_from_link(magnet)
alltorrents = qb.torrents()
tor_hash=""
for torrent in alltorrents:
	print(torrent['magnet_uri'])
	print("elo " + magnet)
	if(torrent['magnet_uri']==magnet):
		tor_hash=torrent['hash']
print(tor_hash)