#!/usr/bin/python
import Ui
import braille

class Temp:
	def __init__(self):
		pass
	def update(self):
		temp=int(Ui.sense.get_temperature())
		humid=int(Ui.sense.get_humidity())

		negativeTemp=(temp < 0)
		temp=abs(temp)

		temp=min(temp,99)
		humid=min(humid,99)

		tempStr=str(temp).rjust(2)
		humidStr=str(humid).rjust(2)+"%"

		tempColor=(255,0,0)
		if(negativeTemp):
			tempColor=(0,0,255)

		braille.printB(0,0,tempStr,fg=tempColor)
		braille.printB(6,0,"C")
		braille.printB(0,4,humidStr)
	def open(self):
		Ui.sense.clear()
		self.update()
	def close(self):
		pass
	def up(self,event):
		if(event.action=="pressed"):
			Ui.resetApp()
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

Ui.registerApp("temp",Temp())
