# -*- coding: utf-8 -*-
import sys
import routing
import logging
import xbmcaddon
from resources.lib import kodiutils
from resources.lib import kodilogging
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory
import urllib
import urlparse
ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()


@plugin.route('/')
def index():
    url = plugin.url_for(search, query="hello world")
    addDirectoryItem(plugin.handle, url, ListItem("Search"))
    endOfDirectory(plugin.handle)


@plugin.route('/category/<category_id>')
def show_category(category_id):
    addDirectoryItem(
        plugin.handle, "", ListItem("Hello category %s!" % category_id))
    endOfDirectory(plugin.handle)

def run():
    plugin.run()

@plugin.route('/search')
def search():
	kb.doModal(2000)


def getusersearch():
	kb = xbmc.Keyboard('default', 'heading')
	kb.setDefault('Enter Search Word')
	kb.setHeading("english" + 'Search')
	kb.setHiddenInput(False)
	kb.doModal()
	if (kb.isConfirmed()):
		search_term = kb.getText()
		return(search_term)
	else:
		return