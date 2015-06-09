import xbmcgui
import xbmcplugin
import xbmc
import xbmcaddon



xbmcplugin.setContent(addon_handle, 'audio')

addon = xbmcaddon.Addon('plugin.audio.air1-radio')
title = addon.getAddonInfo('name')
icon = 'DefaultAddonMusic.png'
url = "rtmp://emf.mpl.miisolutions.net/sa001-high-fms-live01/sa001_mii_edge_high.stream"

li = xbmcgui.ListItem(label=title, iconImage=icon, thumbnailImage=icon, path=url)
li.setInfo(type='music', infoLabels={ "Title": title })
li.setProperty('IsPlayable', 'true')

xbmc.Player().play(item=url, listitem=li)
