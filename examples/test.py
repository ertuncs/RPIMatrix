#!/usr/bin/env python

import max7219.led as led
import max7219.canvas as canvas
import max7219.transitions as transitions
import time

#from random import randrange

#led.init()
#led.show_message("Hello world!", transition = transitions.left_scroll)
def downcounter(start,end,step):
	while end <= start:
		yield start
		start -= step
for x in downcounter(5, 0, 1):
	#canvas.set_on(2,4)
	#canvas.scroll(8)
	time.sleep(0.5)
	led.init()
	#canvas.letter(20)
	led.show_message(str(x),transition = transitions.left_scroll)
	#led.letter(x)
	#canvas.render()
#	print(int(x))
#led.init()

#led.show_message(x, transition = transitions.left_scroll)

#for x in range(256):
#    led.letter(x)
#    time.sleep(0.1)

#while True:
 #   for x in range(500):
 #       canvas.set_on(randrange(8), randrange(8))
 #       canvas.scroll(randrange(16))
 #       canvas.render()
 #       time.sleep(0.01)

 #   for x in range(500):
 #       canvas.set_off(randrange(8), randrange(8))
 #       canvas.scroll(randrange(16))
 #       canvas.render()
 #       time.sleep(0.01)

 #   for x in range(500):
 #       canvas.set_on(4, 4)
 #       canvas.scroll(randrange(8))
 #       canvas.render()
 #       time.sleep(0.01)
