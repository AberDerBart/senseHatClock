#!/usr/bin/python
import Ui

braille={
" ":[[0,0],
     [0,0],
     [0,0]],
"1":[[1,0],
     [0,0],
     [0,0]],
"2":[[1,0],
     [1,0],
     [0,0]],
"3":[[1,1],
     [0,0],
     [0,0]],
"4":[[1,1],
     [1,0],
     [0,0]],
"5":[[1,0],
     [0,1],
     [0,0]],
"6":[[1,1],
     [1,0],
     [0,0]],
"7":[[1,1],
     [1,1],
     [0,0]],
"8":[[1,0],
     [1,1],
     [0,0]],
"9":[[0,1],
     [1,0],
     [0,0]],
"0":[[0,1],
     [1,1],
     [0,0]],
"A":[[1,0],
     [0,0],
     [0,0]],
"B":[[1,0],
     [1,0],
     [0,0]],
"C":[[1,1],
     [0,0],
     [0,0]],
"D":[[1,1],
     [1,0],
     [0,0]],
"E":[[1,0],
     [0,1],
     [0,0]],
"F":[[1,1],
     [1,0],
     [0,0]],
"G":[[1,1],
     [1,1],
     [0,0]],
"H":[[1,0],
     [1,1],
     [0,0]],
"I":[[0,1],
     [1,0],
     [0,0]],
"J":[[0,1],
     [1,1],
     [0,0]],
"K":[[1,0],
     [0,0],
     [1,0]],
"L":[[1,0],
     [1,0],
     [1,0]],
"M":[[1,1],
     [0,0],
     [1,0]],
"N":[[1,1],
     [1,0],
     [1,0]],
"O":[[1,0],
     [0,1],
     [1,0]],
"P":[[1,1],
     [1,0],
     [1,0]],
"Q":[[1,1],
     [1,1],
     [1,0]],
"R":[[1,0],
     [1,1],
     [1,0]],
"S":[[0,1],
     [1,0],
     [1,0]],
"T":[[0,1],
     [1,1],
     [1,0]],
"U":[[1,0],
     [0,0],
     [1,1]],
"V":[[1,0],
     [1,0],
     [1,1]],
"X":[[1,1],
     [0,0],
     [1,1]],
"Y":[[1,1],
     [1,0],
     [1,1]],
"Z":[[1,0],
     [0,1],
     [1,1]],
"&":[[1,1],
     [1,0],
     [1,1]],
"%":[[1,1],
     [1,1],
     [1,1]],
"[":[[1,0],
     [1,1],
     [1,1]],
"ß":[[0,1],
     [1,0],
     [1,1]],
"W":[[0,1],
     [1,1],
     [0,1]]
}

def printB(x,y,text,fg=[255,255,255],bg=[0,0,0],space=1):
	for index,letter in enumerate(text):
		offLetter=index * (space +2)
		for offY, line in enumerate(braille[letter]):
			for offX,draw in enumerate(line):
				if(draw):
					Ui.drawPixel(x+offX+offLetter,y+offY,fg)
				else:
					Ui.drawPixel(x+offX+offLetter,y+offY,bg)

