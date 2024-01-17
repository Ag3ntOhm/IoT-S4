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
while (True) :
    if CSensor.color() == Color.RED :
        ev3.speaker.beep(frequency=440,duration=200)
    if CSensor.color() == Color.BLUE :
        ev3.speaker.beep(frequency=493.88,duration=200)
    if CSensor.color() == Color.WHITE :
        ev3.speaker.beep(frequency=523.25,duration=200)
    if CSensor.color() == Color.BLACK :
        ev3.speaker.beep(frequency=392,duration=200)
    if CSensor.color() == Color.YELLOW :
        ev3.speaker.beep(frequency=311.13,duration=200)
    if CSensor.color() == Color.GREEN :
        ev3.speaker.beep(frequency=554.37,duration=200)
    if CSensor.color() == Color.BROWN :
        ev3.speaker.beep(frequency=329.63,duration=200)
    

