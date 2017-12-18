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
r = [204, 55, 55] #red fire
f = [204, 88, 55] #orange fire

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

drinkingDovahkiin = [[
b, b, b, b, b, b, d, d,
b, b, b, b, b, d, l, l,
b, b, b, b, d, l, l, d,
b, b, b, b, l, l, d, h,
b, b, b, b, e, l, h, h,
b, b, b, b, s, l, h, h,
b, b, b, b, s, d, h, l,
b, b, b, b, l, d, l, l
],[
b, b, b, b, b, b, d, d,
b, b, b, b, b, d, l, l,
b, b, b, b, d, l, l, d,
b, b, b, b, l, l, d, h,
b, b, b, b, e, l, h, h,
b, b, b, b, s, l, h, h,
b, b, b, b, s, d, h, l,
a, a, a, b, l, d, l, l
],[
b, b, b, b, b, b, d, d,
b, b, b, b, b, d, l, l,
b, b, b, b, d, l, l, d,
b, b, b, b, l, l, d, h,
b, b, b, b, e, l, h, h,
b, b, b, b, s, l, h, h,
a, a, a, b, s, d, h, l,
d, d, d, o, l, d, l, l
],[
b, b, b, b, b, b, d, d,
b, b, b, b, b, d, l, l,
b, b, b, b, d, l, l, d,
b, b, b, b, l, l, d, h,
b, b, b, b, e, l, h, h,
a, a, a, b, s, l, h, h,
d, d, d, o, s, d, h, l,
a, a, a, o, l, d, l, l
],[
b, b, b, b, b, b, d, d,
b, b, b, b, b, d, l, l,
b, b, b, b, d, l, l, d,
b, b, b, b, l, l, d, h,
a, a, a, b, e, l, h, h,
d, d, d, o, s, l, h, h,
a, a, a, o, s, d, h, l,
d, d, d, o, l, d, l, l
],[
b, b, b, b, b, b, d, d,
b, b, b, b, b, d, l, l,
b, b, b, b, d, l, l, d,
a, a, a, b, l, l, d, h,
d, d, d, o, e, l, h, h,
a, a, a, o, s, l, h, h,
d, d, d, o, s, d, h, l,
a, a, a, b, l, d, l, l
],[
b, b, b, b, b, b, d, d,
b, b, b, b, b, d, l, l,
b, b, b, b, d, l, l, d,
b, b, b, b, l, l, d, h,
b, a, b, b, e, l, h, h,
a, d, a, h, s, l, h, h,
d, a, d, a, s, d, h, l,
a, d, a, b, l, d, l, l
],[
b, b, b, b, b, b, d, d,
b, b, b, b, b, d, l, l,
b, b, b, b, d, l, l, d,
b, b, b, b, l, l, d, h,
b, a, b, b, e, l, h, h,
a, d, a, h, s, l, h, h,
d, a, d, a, s, d, h, l,
a, d, a, b, l, d, l, l
],[
b, h, l, s, e, d, e, s,
h, h, l, s, s, d, s, s,
d, b, l, s, e, s, e, s,
b, l, b, l, e, e, e, d,
l, l, b, s, a, a, a, a,
l, d, s, a, a, l, a, a,
d, a, s, l, l, d, d, l,
b, b, b, o, a, o, a, b
],[
b, h, l, s, e, d, e, s,
h, h, l, s, s, d, s, s,
d, b, l, s, e, s, e, s,
b, l, b, l, e, e, e, d,
l, l, b, s, a, a, a, a,
l, d, s, a, a, l, a, a,
d, a, s, l, l, d, d, l,
b, b, b, o, a, o, a, b
]]

yolTorShul = [[
h, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, l, b, b, b,
b, b, b, b, l, b, l, h,
b, b, b, b, d, b, d, l,
b, b, b, b, b, s, l, a,
b, b, b, b, b, b, s, a,
b, b, b, b, b, b, o, o
],[
f, h, b, b, b, b, b, b,
h, b, b, b, b, b, b, b,
b, b, b, b, l, b, b, b,
b, b, b, b, l, b, l, h,
b, b, b, b, d, b, d, l,
b, b, b, b, b, s, l, a,
b, b, b, b, b, b, s, a,
b, b, b, b, b, b, o, o
],[
r, f, h, b, b, b, b, b,
f, h, b, b, b, b, b, b,
h, b, b, b, l, b, b, b,
b, b, b, b, l, b, l, h,
b, b, b, b, d, b, d, l,
b, b, b, b, b, s, l, a,
b, b, b, b, b, b, s, a,
b, b, b, b, b, b, o, o
],[
r, r, f, h, b, b, b, b,
r, f, f, h, b, b, b, b,
f, f, h, b, l, b, b, b,
h, h, b, b, l, b, l, h,
b, b, b, b, d, b, d, l,
b, b, b, b, b, s, l, a,
b, b, b, b, b, b, s, a,
b, b, b, b, b, b, o, o
],[
r, r, r, f, f, h, b, b,
r, r, f, f, h, h, b, b,
r, f, f, f, h, b, b, b,
f, f, f, h, h, b, l, h,
f, h, h, h, d, b, d, l,
h, h, b, b, b, s, l, a,
b, b, b, b, b, b, s, a,
b, b, b, b, b, b, o, o
],[
r, r, r, r, f, h, b, b,
r, r, r, r, f, h, h, b,
r, r, r, r, f, f, h, h,
r, r, r, r, r, f, h, h,
f, f, f, r, r, f, f, h,
h, h, f, f, f, f, f, h,
b, h, h, h, f, f, h, h,
b, b, h, h, h, h, h, h
],[
b, b, b, b, b, b, b, b,
b, b, b, b, b, r, r, r,
b, b, b, b, r, r, r, r,
b, b, b, r, r, r, f, f,
b, b, r, r, r, r, f, f,
b, r, r, r, r, f, f, f,
b, r, r, f, f, f, f, f,
b, r, r, f, f, f, f, f
],[
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, h, b,
b, b, b, b, d, d, l, d
]]

entertainment = 100
hunger = 100

while True:
	sense.set_pixels(dovahkiin)
	x,y,z = sense.get_accelerometer_raw().values()
	orientation = sense.get_orientation()

	if (x > 1 or y > 1 or z > 1):
		animate (sense, chargingDovahkiin, .1)
		animate (sense, chargingDovahkiin, .1)
		animate (sense, chargingDovahkiin, .1)
		animate (sense, chargingDovahkiin, .1)
		if (entertainment > 75):
			entertainment = 100
		else:
			entertainment = entertainment + 25
	
	if ((orientation['roll'] > 160 and orientation['roll'] < 180) or (orientation['yaw'] > 200 and orientation['yaw'] < 220)):
		animate (sense, drinkingDovahkiin, .25)
