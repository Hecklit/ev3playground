#!/usr/bin/env python3
from ev3dev.ev3 import *

a = LargeMotor('outA')
b = LargeMotor('outD')

a.run_timed(time_sp=3000, speed_sp=500)
b.run_timed(time_sp=3000, speed_sp=500)
a.run_timed(time_sp=3000, speed_sp=-500)
b.run_timed(time_sp=3000, speed_sp=-500)
