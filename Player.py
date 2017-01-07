import mpd
import Ui
import configparser

class Player:
	client=mpd.MPDClient()
	def __init__(self):
		self.stateImgs={}
		self.stateImgs["play"]=Ui.sense.load_image("img/player/play.png")
		self.stateImgs["pause"]=Ui.sense.load_image("img/player/pause.png")
		self.stateImgs["stop"]=Ui.sense.load_image("img/player/stop.png")
		self.state=None
	def open(self):
		Ui.drawLoading()
		Player.client.connect(Player.host,Player.port)
	def close(self):
		Player.client.disconnect()
	def update(self):
		if("state" in Player.client.status()):
			self.state=Player.client.status()["state"]
		else:
			self.state=None

		if self.state in self.stateImgs:
			Ui.drawImage(self.stateImgs[self.state])
	def down(self,event):
		if(event.action=="pressed"):
			Ui.setApp("playerAdv")
		pass
	def left(self,event):
		if(event.action=='pressed'):
			if(self.state=="pause"):
				Player.client.stop()
			else:
				Player.client.previous()
	def right(self,event):
		if(event.action=='pressed'):
			Player.client.next()
	def middle(self,event):
		if(event.action=='pressed'):
			if(self.state=="pause" or self.state=="stop"):
				Player.client.play()
			elif(self.state=="play"):
				Player.client.pause()
	def up(self,event):
		if(event.action=="pressed"):
			Ui.setApp("idle")



try:
	config=configparser.ConfigParser()
	config.read("senseHatClock.ini")
	Player.host=config.get("player","host")
	Player.port=config.getint("player","port")

	Player.client.connect(Player.host,Player.port)
	Player.client.disconnect()
	Ui.registerApp("player",Player())
except ConnectionRefusedError:
	print("mpd not available")
