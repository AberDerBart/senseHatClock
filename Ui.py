from sense_emu import SenseHat

appDict={}

sense=SenseHat()

selection=None
alpha=1


def pixelAlpha(pixel,alpha):
	"""multiplies the pixel values with [alpha] and return the pixel"""
	return (int(pixel[0]*alpha),int(pixel[1]*alpha),int(pixel[2]*alpha))

def imageAlpha(image,alpha):
	"""takes an image (as pixel array) and multiplies all values with [alpha], returns the multiplied image"""
	alphaImage=[]

	for pixel in image:
		alphaImage.append(pixelAlpha(pixel,alpha))
	
	return alphaImage

def drawImage(image):
	"""draws [image] on the sense hat"""
	sense.set_pixels(imageAlpha(image,alpha))

def drawPixel(x,y,pixel):
	"""sets the pixel color of pixel at ([x],[y]) on the sense hat to [pixel]"""
	global alpha
	sense.set_pixel(x,y,pixelAlpha(pixel,alpha))

def drawLoading():
	"""draws a loading icon on the sense hat"""
	drawImage(drawLoading.loading)

drawLoading.loading=sense.load_image("img/loading.png")


def registerApp(appString,app):
	"""registers [app] in [appDict], it can then be loaded with [setApp]"""
	appDict[appString]=app

def setApp(appString):
	"""loads app with the corresponding string [appString]"""
	global appDict
	global selection
	if appString in appDict.keys():
		if selection:
			selection.close()
		selection=appDict[appString]
		selection.open()

def resetApp():
	"""returns to the idle app"""
	setApp("idle")

# define update
def update():
	"""main loop iteration - executes the update method in the current app and processes keypresses"""
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

	if(update.ticks > 70):
		resetApp()
update.ticks=0
