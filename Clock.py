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
		self.sense.clear()
		braille.printB(Ui.sense,0,0,hourString)
		braille.printB(Ui.sense,3,4,minString)
	def open(self):
		pass
	def close(self):
		pass
	def down(self,event):
		pass
	def left(self,event):
		pass
	def right(self,event):
		pass
	def middle(self,event):
		pass

Ui.registerApp("clock",Clock())
