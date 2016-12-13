from sense_emu import SenseHat

sense=SenseHat()

braille={"a":[[1,0],
              [0,0],
	      [0,0]],
"b":[[1,0],
     [1,0],
     [0,0]],
"c":[[1,1],
     [0,0],
     [0,0]],
"d":[[1,1],
     [1,0],
     [0,0]],
"e":[[1,0],
     [0,1],
     [0,0]],
"f":[[1,0],
     [0,0],
     [0,0]],
"g":[[1,0],
     [0,0],
     [0,0]],
"h":[[1,0],
     [0,0],
     [0,0]],
"i":[[1,0],
     [0,0],
     [0,0]],
"j":[[1,0],
     [0,0],
     [0,0]]
}

def printB(sense,x,y,text,fg=[255,0,0],bg=[0,0,0]):
	for offY, line in enumerate(braille[text]):
		for offX,draw in enumerate(line):
			if(draw):
				sense.set_pixel(x+offX,y+offY,fg)
				print("("+str(x+offX)+","+str(y+offY)+")")
			else:
				sense.set_pixel(x+offX,y+offY,bg)
				print("n("+str(x+offX)+","+str(y+offY)+")")

