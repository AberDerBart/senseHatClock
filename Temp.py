#!/usr/bin/python
import braille

class Temp:
	def __init__(self,sense):
		self.sense=sense
	def update(self):
		temp=int(self.sense.get_temperature())
		humid=int(self.sense.get_humidity())

		negativeTemp=(temp < 0)
		temp=abs(temp)

		temp=min(temp,99)
		humid=min(humid,99)

		tempStr=str(temp).rjust(2)+"C"
		humidStr=str(humid).rjust(2)+"%"
		print(tempStr)
		print(humidStr)

		self.sense.clear()
		braille.printB(self.sense,0,0,tempStr)
		braille.printB(self.sense,0,4,humidStr)


	def up(self):
		pass
	def down(self):
		pass
	def left(self):
		pass
	def right(self):
		pass
	def center(self):
		pass