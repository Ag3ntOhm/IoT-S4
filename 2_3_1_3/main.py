#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

bob = DriveBase(left_motor, right_motor, wheel_diameter = 54, axle_track = 121)
TSensor = TouchSensor(Port.S1)

count = 0
now = time.time()
then = now + 5
ev3.screen.print(count)
while (time.time() < then) :
    if (TSensor.pressed()) : 
        count += 1
        ev3.screen.print(count)
        wait(150)

for i in range(count) :
    ev3.speaker.beep(frequency=440, duration=500)
    wait(500)