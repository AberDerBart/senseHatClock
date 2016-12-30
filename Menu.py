#!/usr/bin/python
import Ui

class Menu:
	def __init__(self,imgPath=None,leftAction=None,rightAction=None,upAction=None,downAction=None,middleAction=None):
		if(imgPath):
			self.img=Ui.sense.load_image(imgPath)
		else:
			self.img=None
		self.leftAction=leftAction
		self.rightAction=rightAction
		self.upAction=upAction
		self.downAction=downAction
		self.middleAction=middleAction
	def open(self):
		if(self.img):
			Ui.drawImage(self.img)
		else:
			Ui.sense.clear()
	def close(self):
		pass
	def update(self):
		pass
	def down(self,event):
		if(self.downAction and event.action=="pressed"):
			Ui.setApp(self.downAction)
	def left(self,event):
		if(self.leftAction and event.action=="pressed"):
			Ui.setApp(self.leftAction)
	def right(self,event):
		if(self.rightAction and event.action=="pressed"):
			Ui.setApp(self.rightAction)
	def middle(self,event):
		if(self.middleAction and event.action=="pressed"):
			Ui.setApp(self.middleAction)
	def up(self,event):
		if(self.upAction and event.action=="pressed"):
			Ui.setApp(self.upAction)
