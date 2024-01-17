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
def add(color, L) :
    if (color == Color.YELLOW) :
        L[0] += 1
    if (color == Color.BLUE) :
        L[1] += 1
    if (color == Color.RED) :
        L[2] += 1

def show(L) :
    ev3.screen.print("Yellow: " + str(L[0]))
    ev3.screen.print("Blue: " + str(L[1]))
    ev3.screen.print("Red: " + str(L[2]))
    print("Yellow: " + str(L[0]))
    print("Blue: " + str(L[1]))
    print("Red: " + str(L[2]))

def sing(s) :
    for x in s :
        if (x == Color.YELLOW) :
            ev3.speaker.beep(frequency=443.23,duration=500)
        if (x == Color.BLUE) :
            ev3.speaker.beep(frequency=392,duration=500)
        if (x == Color.RED) :
            ev3.speaker.beep(frequency=440,duration=500)

# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

bob = DriveBase(left_motor, right_motor, wheel_diameter = 54, axle_track = 121)
CSensor = ColorSensor(Port.S3)
TSensor = TouchSensor(Port.S1)

last = None
bob.drive(100,0)
L = [0,0,0]
s = []
while (not TSensor.pressed()) :
    cs = CSensor.color()
    if (cs == Color.BLACK or cs == Color.WHITE):
        last = cs
    if (cs!= None and cs != last) :
        add(cs,L)
        s.append(cs)
        last = cs
        show(L)

bob.stop()
sing(s)
