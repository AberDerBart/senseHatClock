import mpd
import Ui
from Player import Player
import Menu

class PlayerVolume:
	def __init__(self):
		self.image=Ui.sense.load_image("img/playerAdvanced/volume.png")
	def open(self):
		Ui.drawLoading()
		Player.client.connect(Player.host,Player.port)
		self.volume=None
		Ui.drawImage(self.image)
		self.update()
	def close(self):
		Player.client.disconnect()
	def update(self):
		if("volume" in Player.client.status()):
			self.volume=int(Player.client.status()["volume"])
		for x in range(0,8):
			if(self.volume >= 12.5*x):
				Ui.drawPixel(x,7,(255,255,255))
			else:
				Ui.drawPixel(x,7,(0,0,0))
	def down(self,event):
		pass
	def left(self,event):
		if(event.action=='pressed'):
			Player.client.setvol(max(self.volume-1,0))
	def right(self,event):
		if(event.action=='pressed'):
			Player.client.setvol(min(self.volume+1,100))
	def middle(self,event):
		pass
	def up(self,event):
		if(event.action=="pressed"):
			Ui.setApp("player")

Ui.registerApp("volume",PlayerVolume())
