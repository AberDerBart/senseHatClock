#!/usr/bin/python

import Ui
import Clock
import Temp
import Player
import Menu

import time

Ui.registerApp("idle",Menu.Menu(upAction="clock",downAction="player",leftAction="temp"))

Ui.setApp("idle")
run=True

while(run):
	time.sleep(.1)
	Ui.update()



	
