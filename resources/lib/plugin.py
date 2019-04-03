# -*- coding: utf-8 -*-
import sys
import routing
import logging
import xbmcaddon
from resources.lib import kodiutils
from resources.lib import kodilogging
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory
import urlparse
import xbmc
import main
import qbit
import re
import site_parsing
ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()

qbitIP='192.168.0.101:8080'

@plugin.route('/')
def index():
    addDirectoryItem(plugin.handle, plugin.url_for(show_category), ListItem("Add torrent (search)"), True)
    # addDirectoryItem(plugin.handle, plugin.url_for(qbitIP), ListItem("Change IP of qbittorrent client"), True)
    # addDirectoryItem(plugin.handle, plugin.url_for(qbitmenu), ListItem("Browse torrents"), True)
    endOfDirectory(plugin.handle)

@plugin.route('/category')
def show_category():
	keyboard = xbmc.Keyboard('', 'Search something')
	keyboard.doModal()
	input_text = keyboard.getText()
	names_and_sources = main.get_items("https://torrentz2.eu/search?f=" + str(input_text))
	z=1
	y=[]
	for x in names_and_sources:
		x = re.sub(r'https://torrentz2.eu/', '', x)
		if(z%6!=0):
			y.append(x)
		else:
			info = (str(y[2]+", "+str(y[3] + ", seeds: " + str(y[4]))))
			addDirectoryItem(plugin.handle,plugin.url_for(activate, y[1]), ListItem(str(y[0])))
			addDirectoryItem(plugin.handle,plugin.url_for(activate, y[1]), ListItem(info))
			y=[]
		z+=1
	endOfDirectory(plugin.handle)

@plugin.route('/qbitmenu')
def qbitmenu():
	addDirectoryItem(plugin.handle, "", ListItem("Nothing yet"), True)
	endOfDirectory(plugin.handle)

@plugin.route('/activate/<link>')
def activate(link):
	xbmc.executebuiltin('Notification('+str(link)+',Added,/script.hellow.world.png)')
	magnet = site_parsing.link_to_magnet("https://torrentz2.eu/"+link)
	qbit.add_torrent(magnet)

def run():
    plugin.run()