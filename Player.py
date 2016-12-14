import mpd

class Player:
	def __init__(self,sense):
		self.sense=sense
		self.client=mpd.MPDClient()
		self.stateImgs={}
		self.stateImgs["play"]=sense.load_image("playerPlay.png")
		self.stateImgs["pause"]=sense.load_image("playerPause.png")
		self.stateImgs["stop"]=sense.load_image("playerStop.png")
	def open(self):
		self.client.connect("localhost",6600)
	def close(self):
		self.client.close()
	def update(self):
		state=self.client.status()["state"]
		if state in self.stateImgs:
			self.sense.set_pixels(self.stateImgs[state])
	def down(self,event):
		pass
	def left(self,event):
		if(event.action=='pressed'):
			self.client.previous()
	def right(self,event):
		if(event.action=='pressed'):
			self.client.next()
	def center(self,event):
		if(event.action=='pressed'):
			self.client.pause()
