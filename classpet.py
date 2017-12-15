from sense_hat import SenseHat
import time

#animate function
def animate(sense, slides, sleeptime):
	for slide in slides:
		sense.set_pixels(slide)
		time.sleep(sleeptime)

#instantiation of SenseHat object
sense = SenseHat()

#color rgb values used in animations
h = (216, 157, 28) #horn
l = (100, 100, 115) #light metal
d = (70, 70, 85) #dark metal
s = (216, 180, 88) #skin
a = (96, 66, 25) #armor
o = (136, 86, 35) #shoe leather
e = (0, 0, 0) #eyes and mouth
b = (180, 180, 180) #background

#idle avatar
dovahkiin = [
b, h, l, s, e, d, e, s,
h, h, l, s, s, d, s, s,
d, b, l, s, e, e, e, s,
b, l, b, l, s, s, s, d,
l, l, b, s, a, a, a, a,
l, d, s, a, a, l, a, a,
d, a, s, l, l, d, d, l,
b, b, b, o, a, o, a, b
]

#entertain animation
chargingDovahkiin = [[
b, h, l, s, e, d, e, s,
h, h, l, s, s, d, s, s,
d, b, l, s, e, e, e, s,
b, l, b, l, e, e, e, d,
l, l, b, s, a, a, a, a,
l, d, s, a, a, l, a, a,
d, a, s, l, l, d, d, l,
b, b, b, o, a, o, a, b
],[
b, b, l, l, d, d, d, l,
b, h, l, s, e, d, e, s,
h, h, l, s, s, d, s, s,
d, b, l, s, e, e, e, s,
b, l, b, l, e, e, e, d,
l, l, s, a, a, l, a, a,
l, d, s, l, l, d, d, l,
d, a, b, o, o, a, b, b
],[
b, h, l, s, e, d, e, s,
h, h, l, s, s, d, s, s,
d, b, l, s, e, e, e, s,
b, l, b, l, e, e, e, d,
l, l, b, s, a, a, a, a,
l, d, s, a, a, l, a, a,
d, a, s, l, l, d, d, l,
b, b, b, o, a, o, a, b
],[
b, b, l, l, d, d, d, l,
b, h, l, s, e, d, e, s,
h, h, l, s, s, d, s, s,
d, b, l, s, e, e, e, s,
b, l, b, l, e, e, e, d,
l, l, s, a, a, l, a, a,
l, d, s, l, l, d, d, l,
d, a, b, o, a, b, o, a
]]

#feeding animation
feastingDovahkiin = [[

]]

while True:
	sense.set_pixels(dovahkiin)
	x,y,z = sense.get_accelerometer_raw().values()
	orientation = sense.get_orientation()

	if (x > 1 or y > 1 or z > 1):
		animate (sense, chargingDovahkiin, .1)
		animate (sense, chargingDovahkiin, .1)
		animate (sense, chargingDovahkiin, .1)
		animate (sense, chargingDovahkiin, .1)
	
	if ((orientation['roll'] > 160 and orientation['roll'] < 180) or (orientation['yaw'] > 200 and orientation['yaw'] < 220)):
		animate (sense, feastingDovahkiin, .5)
