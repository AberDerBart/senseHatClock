from sense_emu import SenseHat

appDict={}

sense=SenseHat()

selection=None

def registerApp(appString,app):
	appDict[appString]=app

def setApp(app):
	global appDict
	global selection
	if app in appDict.keys():
		if selection:
			selection.close()
		selection=appDict[app]
		selection.open()

def resetApp():
	setApp("idle")

# define keybindings
def down(event):
	selection.down(event)
def left(event):
	selection.left(event)
def right(event):
	selection.right(event)
def middle(event):
	selection.middle(event)
def up(event):
	selection.up(event)

# define update
def update():
	update.ticks=update.ticks+1
	selection.update()
	for event in sense.stick.get_events():
		if(event.direction=="left"):
			selection.left(event)
		if(event.direction=="right"):
			selection.right(event)
		if(event.direction=="up"):
			selection.up(event)
		if(event.direction=="down"):
			selection.down(event)
		if(event.direction=="middle"):
			selection.middle(event)
		update.ticks=0

	if(update.ticks > 30):
		resetApp()
update.ticks=0
