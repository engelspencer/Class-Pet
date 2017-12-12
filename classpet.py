from sense_hat import SenseHat
import time

def animate(sense, slides, sleeptime):
	for slide in slides:
		sense.set_pixels(slide)
		time.sleep(sleeptime)

sense = SenseHat()

h = (204, 157, 55) #horn
l = (122, 122, 122) #light metal
d = (85, 85, 85) #dark metal
s = (234, 206, 138) #skin
a = (125, 86, 33) #armor
e = (0, 0, 0) #eyes and mouth
b = (205, 205, 205) #background

knight = [[
	b, h, l, s, e, d, e, s,
	h, h, l, s, s, d, s, s,
	d, b, l, s, e, e, e, s,
	b, l, b, l, s, s, s, d,
	l, l, b, s, a, a, a, a,
	l, d, s, a, a, l, a, a,
	d, a, s, l, l, d, d, l,
	b, b, b, a, a, b, a, a
	],[
	

while True:
	
