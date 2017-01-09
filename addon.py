import xbmcaddon
import os

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

os.system("google-chrome --start-fullscreen --disable-session-crashed-bubble --kiosk http://primevideo.com")
