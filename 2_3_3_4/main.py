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
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

bob = DriveBase(left_motor, right_motor, wheel_diameter = 54, axle_track = 121)
CSensor = ColorSensor(Port.S3)

angle = 10
sym = 5
speed = 250
bob.drive(250,0)

while (CSensor.color() != Color.RED) :
    print(CSensor.color())
    if (CSensor.color() == Color.BLACK) :
        bob.drive(250,0)
        angle = 10
        speed = 250
        sym = 10
    elif (CSensor.color() == Color.BLUE) :
        bob.drive(100,0)
        speed = 100
        angle = 10
        sym = 10
    else :
        for i in range(sym) :
            if (CSensor.color() == Color.BLACK or CSensor.color() == Color.BLUE) :
                break
            bob.turn(2)
        for i in range(sym + sym/2) :
            if (CSensor.color() == Color.BLACK or CSensor.color() == Color.BLUE) :
                break
            bob.turn(-2)
        sym += 2
        

