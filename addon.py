import sys
import xbmcgui
import xbmcplugin
import xbmc
import xbmcaddon

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')

addon = xbmcaddon.Addon('plugin.audio.air1-radio')
title = addon.getAddonInfo('name')
#icon = addon.getAddonInfo('icon')
url = "rtmp://emf.mpl.miisolutions.net/sa001-high-fms-live01/sa001_mii_edge_high.stream"

li = xbmcgui.ListItem(label=title, path=url)
li.setInfo(type='Audio', infoLabels={ "Title": title })
li.setProperty('IsPlayable', 'true')

xbmc.Player().play(item=url, listitem=li)
