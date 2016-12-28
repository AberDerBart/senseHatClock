from sense_emu import SenseHat
import Clock
import Temp
import Player
import time

sense=SenseHat()

run=True

sleepImage=sense.load_image("sleep.png")
alarmImage=sense.load_image("alarm.png")
ctlImage=sense.load_image("ctl.png")
volImage=sense.load_image("vol.png")

selection=None

clock=Clock.Clock(sense)
temp=Temp.Temp(sense)
player=Player.Player(sense)

selection=player
selection=clock

def down(event):
	selection.down(event)
def left(event):
	selection.left(event)
def right(event):
	selection.right(event)
def middle(event):
	selection.middle(event)

selection.open()
sense.stick.direction_left=left
sense.stick.direction_right=right
sense.stick.direction_down=down
sense.stick.direction_middle=middle


while(run):
	time.sleep(.1)
	selection.update()



	
