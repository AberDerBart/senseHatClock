#!/usr/bin/python
import time
import braille

class Clock:
	def __init__(self,sense):
		self.sense=sense
	def update(self):
		localTime=time.localtime()
		hourString=str(localTime.tm_hour).rjust(2,'0')
		minString=str(localTime.tm_min).rjust(2,'0')
		self.sense.clear()
		braille.printB(self.sense,0,0,hourString)
		braille.printB(self.sense,3,4,minString)
	def open(self):
		pass
	def close(self):
		pass
	def down(self):
		pass
	def left(self):
		pass
	def right(self):
		pass
	def middle(self):
		pass
