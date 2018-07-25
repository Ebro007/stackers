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
		y =7
		win =0
		pygame.time.set_timer(USEREVENT +1, 800)
		while self.gaming:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if y ==7:
						win = x
					else:
						if y == 0:
							if x == win:
								print 'You Win!'
								print 'Congratulations!'
								self.gaming = False
								sense.clear()
						else:
							if x == win:
								print 'Great!'
							else:
								print 'You Lose!'
								self.gaming = False
								sense.clear()

					sense.set_pixel(x, y, (255, 0, 125))
#					self.gaming = False
#					print 'hi'
					if self.gaming == True:					
						y = y-1
						x = 0
#					if self.gaming == False:
#						self.gaming = True
						
					
				else:
					sense.set_pixel(x, y, (255, 0, 125))
					time.sleep(0.3)
					sense.set_pixel(x, y, (0, 0, 0))
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
