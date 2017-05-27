#!/usr/bin/env python3
from ev3dev.ev3 import *

running = True
a = LargeMotor('outA')
b = LargeMotor('outB')
ts = TouchSensor()
ir = ColorSensor()
while running:
    if ir.color == 6:
        a.run_forever(speed_sp=500)
        b.run_forever(speed_sp=500)
    else:
        a.run_forever(speed_sp=-500)
        b.run_forever(speed_sp=0)
    if ts.value() == 1:
        a.reset()
        b.reset()
        running = False
