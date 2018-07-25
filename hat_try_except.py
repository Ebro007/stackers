from sense_hat import SenseHat
import time

#script

sense = SenseHat()
sense.clear()

def loop():
	while True:
		sense.set_pixel(1, 6, (255, 0, 125))
		time.sleep(.001)
		sense.set_pixel(1, 6, (255, 0, 125))
		time.sleep(.001)

if __name__ == "__main__":
	try:
		loop()
	except KeyboardInterrupt:
		sense.clear()
