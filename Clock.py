#!/usr/bin/python
import time
import braille

import Ui

class Clock:
	def __init__(self):
		pass
	def update(self):
		localTime=time.localtime()
		hourString=str(localTime.tm_hour).rjust(2,'0')
		minString=str(localTime.tm_min).rjust(2,'0')
		braille.printB(0,0,hourString)
		braille.printB(3,4,minString)
	def open(self):
		Ui.sense.clear()
		pass
	def close(self):
		pass
	def down(self,event):
		if(event.action=="pressed"):
			Ui.resetApp()
	def left(self,event):
		if(event.action=="pressed"):
			Ui.resetApp()
	def right(self,event):
		if(event.action=="pressed"):
			Ui.resetApp()
	def middle(self,event):
		if(event.action=="pressed"):
			Ui.resetApp()
	def up(self,event):
		if(event.action=="pressed"):
			Ui.resetApp()

Ui.registerApp("clock",Clock())
