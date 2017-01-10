#!/usr/bin/python
import mpd
import Ui
from Player import Player
import Menu
import TimeSelect
import Volume

def alarm(hour,minute):
	"""set an alarm timer for [hour]:[minute]"""
	Ui.drawLoading()

	Player.client.connect(Player.host,Player.port)
	Player.client.sendmessage("scheduler","alarm "+str(hour)+":"+str(minute))
	Player.client.disconnect()

	print("Alarm: "+str(hour)+":"+str(minute))
	Ui.setApp("player")

def sleep(hour, minute):
	"""set a sleep timer for [hour]:[minute]"""
	Ui.drawLoading()

	Player.client.connect(Player.host,Player.port)
	Player.client.sendmessage("scheduler","sleep "+str(hour)+":"+str(minute))
	Player.client.disconnect()

	print("Sleep: "+str(hour)+":"+str(minute))
	Ui.setApp("player")


try:
	Player.client.connect(Player.host,Player.port)
	if("scheduler" in Player.client.channels()):
		Ui.registerApp("playerAdv",Menu.Menu("img/playerAdvanced/menu.png",upAction="player",rightAction="playerSleep",leftAction="playerAlarm",downAction="volume"))
		Ui.registerApp("playerAlarm",TimeSelect.TimeSelect(alarm,imgPath="img/playerAdvanced/alarm.png",rightAction="playerAdv",leftAction="playerAdv"))
		Ui.registerApp("playerSleep",TimeSelect.TimeSelect(sleep,imgPath="img/playerAdvanced/sleep.png",leftAction="playerAdv",rightAction="playerAdv"))
		
	else:
		print("mpdScheduler not available")
		Ui.registerApp("playerAdv",Ui.getApp("volume"))

	Player.client.disconnect()
except ConnectionRefusedError:
	pass
