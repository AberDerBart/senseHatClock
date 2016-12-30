import Ui
import braille
import time

class TimeSelect:
	def __init__(self,func,imgPath=None,leftAction=None, rightAction=None):
		if(imgPath):
			self.img=Ui.sense.load_image(imgPath)
		else:
			self.img=None
		self.leftAction=leftAction
		self.rightAction=rightAction
		self.func=func
	def open(self):
		self.hour=time.localtime().tm_hour
		self.minute=time.localtime().tm_min
		self.selection=0

		if(self.img):
			Ui.drawImage(self.img)
		else:
			Ui.sense.clear()

		self.update()
	def close(self):
		pass
	def update(self):
		blink=(time.time()%1 >= .5)
		hourString=str(self.hour).rjust(2,'0')
		minString=str(self.minute).rjust(2,'0')

		if(blink):
			braille.printB(3,0,hourString)
			braille.printB(3,4,minString)
		elif(self.selection==0):
			braille.printB(3,0,"  ")
			braille.printB(3,4,minString)
		elif(self.selection==1):
			braille.printB(3,0,hourString)
			braille.printB(3,4,"  ")
	def down(self,event):
		if(event.action=="pressed"):
			if(self.selection==0):
				self.hour=(self.hour-1)%24
			elif(self.selection==1):
				self.minute=(self.minute-1)%60
	def up(self,event):
		if(event.action=="pressed"):
			if(self.selection==0):
				self.hour=(self.hour+1)%24
			elif(self.selection==1):
				self.minute=(self.minute+1)%60
	def left(self,event):
		if(event.action=="pressed"):
			self.selection=self.selection-1
			if(self.selection < 0):
				if(self.leftAction):
					Ui.setApp(self.leftAction)
				else:
					self.selection=1
	def right(self,event):
		if(event.action=="pressed"):
			self.selection=self.selection+1
			if(self.selection > 1):
				if(self.rightAction):
					Ui.setApp(self.rightAction)
				else:
					self.selection=0
	def middle(self,event):
		if(event.action=="pressed"):
			self.func(self.hour,self.minute)
