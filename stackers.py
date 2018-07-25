from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time

sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640, 480))
		self.gaming = True

	def startGame(self):
		x =0
		pygame.time.set_timer(USEREVENT +1, 800)
		while self.gaming:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					sense.set_pixel(x, 7, (255, 0, 125))
					self.gaming = False
					print 'hi'	
				else:
					sense.set_pixel(x, 7, (255, 0, 125))
					time.sleep(0.3)
					sense.set_pixel(x, 7, (0, 0, 0))
					time.sleep(0.3)
					if x == 7:
						x = 0
					else:
						x = x +1
				
				
				
if __name__=="__main__":
	try:	
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
