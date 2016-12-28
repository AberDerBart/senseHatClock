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
	def down(self):
		pass
	def left(self):
		pass
	def right(self):
		pass
	def middle(self):
		pass

Ui.registerApp("idle",Idle())
