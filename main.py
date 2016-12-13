from sense_emu import SenseHat

sense=SenseHat()

run=True

while(run):
	event=sense.stick.wait_for_event()

