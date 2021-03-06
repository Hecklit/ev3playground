#!/usr/bin/env python3
from ev3dev.ev3 import *



a.run_timed(time_sp=3000, speed_sp=500)
b.run_timed(time_sp=3000, speed_sp=500)
a.run_timed(time_sp=3000, speed_sp=-500)
b.run_timed(time_sp=3000, speed_sp=-500)

colors = {
    0: 'No color',
    1: 'Black',
    2: 'Blue',
    3: 'Green',
    4: 'Yellow',
    5: 'Red',
    6: 'White',
    7: 'Brown',
}
while True:
    print(colors[ir.color])

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
