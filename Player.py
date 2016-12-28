import mpd

class Player:
	def __init__(self,sense):
		self.sense=sense
		self.client=mpd.MPDClient()
		self.stateImgs={}
		self.stateImgs["play"]=sense.load_image("playerPlay.png")
		self.stateImgs["pause"]=sense.load_image("playerPause.png")
		self.stateImgs["stop"]=sense.load_image("playerStop.png")
		self.state=None
	def open(self):
		self.client.connect("localhost",6600)
	def close(self):
		self.client.close()
	def update(self):
		if("state" in self.client.status()):
			self.state=self.client.status()["state"]
		else:
			self.state=None

		if self.state in self.stateImgs:
			self.sense.set_pixels(self.stateImgs[self.state])
	def down(self,event):
		pass
	def left(self,event):
		if(event.action=='pressed'):
			if(self.state=="pause"):
				self.client.stop()
			else:
				self.client.previous()
	def right(self,event):
		if(event.action=='pressed'):
			self.client.next()
	def middle(self,event):
		if(event.action=='pressed'):
			if(self.state=="pause" or self.state=="stop"):
				self.client.play()
			elif(self.state=="play"):
				self.client.pause()
