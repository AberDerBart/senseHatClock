#!/usr/bin/python
import mpd
import Ui
import Player
import Menu
import TimeSelect

Ui.registerApp("playerAdv",Menu.Menu("img/advanced.png",upAction="player",rightAction="playerSleep",leftAction="playerAlarm"))

def alarm(hour,minute):
	print("Alarm: "+str(hour)+":"+str(minute))
	Ui.setApp("player")

def sleep(hour, minute):
	print("Sleep: "+str(hour)+":"+str(minute))
	Ui.setApp("player")

Ui.registerApp("playerAlarm",TimeSelect.TimeSelect(alarm,imgPath="img/alarm.png",rightAction="playerAdv"))
Ui.registerApp("playerSleep",TimeSelect.TimeSelect(sleep,imgPath="img/sleep.png",leftAction="playerAdv"))
