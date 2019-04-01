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
ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()


sample_input=('[HorribleSubs] One Piece - 878 [1080p].mkv', '/ec4151463c207bb0e675c019a12cd6e47a448f99')+('[HorribleSubs] One Piece - 878 [720p].mkv', '/8668757659662a730413f8c13d66d838427e634d')+('Ester Dean - One Piece.mp3', '/f9290b830c2b4fd5578fe667997ab5172cfc9698')+('[ www.Torrent9.uno ] Earth.One.Amazing.Day.2017.FRENCH.BDRip.XviD-EXTREME.avi', '/bb3fa8d52f093bd95290ba437be00a0872e7402b')
('One Piece 823.cbr', '/4844869777b637b4719c3ac93e82ac9abe30d282')
('[HorribleSubs] One Piece - 878 [480p].mkv', '/d7bda5273a19d9f410db31e52e49fd29d1ddc992')
('[HorribleSubs] One Piece - 877 [1080p].mkv', '/61cdd774c5102767bf32d4ac422c059605ed2796')
('[ www.Torrent9.uno ] [Shin Sekai] One Piece - 878 VOSTFR HD.mp4', '/1883f269c633f66a9559251a33ffb7eea5701f19')
('[HorribleSubs] One Piece - 877 [720p].mkv', '/a77eaf95803584e85b3e3ad8e65569d96ecbf83f')



@plugin.route('/')
def index():
    addDirectoryItem(plugin.handle, plugin.url_for(show_category), ListItem("Category One"), True)
    endOfDirectory(plugin.handle)

@plugin.route('/category')
def show_category():
	klawiatura = xbmc.Keyboard('default', 'heading')
	klawiatura.doModal()
	tekst =	klawiatura.getText()
	xbmc.executebuiltin('Notification(Wpisales:,'+str(tekst)+',5000,/script.hellow.world.png)')
	i=2
	for x in sample_input:
		if(i%2==0):
			addDirectoryItem(plugin.handle, "", ListItem(str(x)))
		i+=1
	endOfDirectory(plugin.handle)



def run():
    plugin.run()