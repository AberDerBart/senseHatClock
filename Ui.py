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

# define keybindings
def down(event):
	selection.down(event)
def left(event):
	selection.left(event)
def right(event):
	selection.right(event)
def middle(event):
	selection.middle(event)

# define update
def update():
	selection.update()

# set keybinding
sense.stick.direction_left=left
sense.stick.direction_right=right
sense.stick.direction_down=down
sense.stick.direction_middle=middle
