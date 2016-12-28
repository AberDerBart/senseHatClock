#!/usr/bin/python

import Ui

class Idle:
	def __init__(self):
		pass
	def update(self):
		pass
	def open(self):
		Ui.sense.clear()
		pass
	def close(self):
		pass
	def down(self,event):
		if(event.action=="pressed"):
			Ui.setApp("player")
	def left(self,event):
		if(event.action=="pressed"):
			Ui.setApp("temp")
	def right(self,event):
		pass
	def middle(self,event):
		pass
	def up(self,event):
		if(event.action=="pressed"):
			Ui.setApp("clock")
		pass

Ui.registerApp("idle",Idle())
