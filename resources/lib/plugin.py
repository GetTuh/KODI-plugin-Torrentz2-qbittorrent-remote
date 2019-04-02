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
	xbmc.executebuiltin('Notification(Wpisales:,'+str(input_text)+',5000,/script.hellow.world.png)')
	names_and_sources = main.get_items("https://torrentz2.eu/search?f=" + str(input_text))
	i=2
	for x in names_and_sources:
		addDirectoryItem(plugin.handle, "", ListItem(str(x)))
		i+=1
	endOfDirectory(plugin.handle)

@plugin.route('/qbitmenu')
def qbitmenu():
	addDirectoryItem(plugin.handle, "", ListItem("jestes zjebany"), True)
	endOfDirectory(plugin.handle)

def run():
    plugin.run()