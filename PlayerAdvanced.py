#!/usr/bin/python
import mpd
import Ui
from Player import Player
import Menu
import TimeSelect

def alarm(hour,minute):
	"""set an alarm timer for [hour]:[minute]"""

	Player.client.connect("localhost",6600)
	Player.client.sendmessage("scheduler","alarm "+str(hour)+":"+str(minute))
	Player.client.disconnect()

	print("Alarm: "+str(hour)+":"+str(minute))
	Ui.setApp("player")

def sleep(hour, minute):
	"""set a sleep timer for [hour]:[minute]"""

	Player.client.connect("localhost",6600)
	Player.client.sendmessage("scheduler","sleep "+str(hour)+":"+str(minute))
	Player.client.disconnect()

	print("Sleep: "+str(hour)+":"+str(minute))
	Ui.setApp("player")


try:
	Player.client.connect("localhost",6600)
	if("scheduler" in Player.client.channels()):
		Ui.registerApp("playerAdv",Menu.Menu("img/advanced.png",upAction="player",rightAction="playerSleep",leftAction="playerAlarm"))
		Ui.registerApp("playerAlarm",TimeSelect.TimeSelect(alarm,imgPath="img/alarm.png",rightAction="playerAdv"))
		Ui.registerApp("playerSleep",TimeSelect.TimeSelect(sleep,imgPath="img/sleep.png",leftAction="playerAdv"))
		
	else:
		print("mpdScheduler not available")

	Player.client.disconnect()
except ConnectionRefusedError:
	pass
