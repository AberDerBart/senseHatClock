from sense_emu import SenseHat
import Clock
import Temp

sense=SenseHat()

run=True

sleepImage=sense.load_image("sleep.png")
alarmImage=sense.load_image("alarm.png")
ctlImage=sense.load_image("ctl.png")
volImage=sense.load_image("vol.png")

selection=None

directionMap={
	'right':sleepImage,
	'left':alarmImage,
	'up':ctlImage,
	'down':volImage,
	'middle':None
}

clock=Clock.Clock(sense)
temp=Temp.Temp(sense)

while(run):
	event=sense.stick.wait_for_event()
	
	# update the selected menu
	if(event.action=='pressed'):
		selection=directionMap[event.direction]

	if(selection):
		sense.set_pixels(selection)
	else:
		temp.update()



	
