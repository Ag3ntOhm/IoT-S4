#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
while (True) :
    butt = ev3.buttons.pressed()
    if (butt != None and len(butt) != 0) :
        if (butt[0] == Button.CENTER) :
            ev3.speaker.beep(frequency=440,duration=200)
        if (butt[0] == Button.RIGHT) :
            ev3.speaker.beep(frequency=493.88,duration=200)
        if (butt[0] == Button.LEFT) :
            ev3.speaker.beep(frequency=523.25,duration=200)
        if (butt[0] == Button.UP) :
            ev3.speaker.beep(frequency=392,duration=200)
        if (butt[0] == Button.DOWN) :
            ev3.speaker.beep(frequency=311.13,duration=200)

