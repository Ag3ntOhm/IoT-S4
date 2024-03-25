#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from umqtt.robust import MQTTClient
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# MQTT setup
MQTT_ClientID = 'S'
MQTT_Broker = '192.168.141.244'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


bob = DriveBase(left_motor, right_motor, wheel_diameter = 54, axle_track = 105)


# List to store triggers
trig = []
dif = 0.1


def listen() :
    pass


def diff(x, y) :
    return (y > x * (1 + dif) or y < x * (1 - dif))



# Write your program here.
client.connect()
time.sleep(0.5)
ev3.screen.print('Started')
client.set_callback(listen) 
client.subscribe(MQTT_Topic_Status) 
time.sleep(0.5)
ev3.screen.print('Listening')

UltraSensor = UltrasonicSensor(Port.S4)
start  = time.time()
check_rate = 0.5

base = UltraSensor.distance()

while True :
    if (time.time() > start + check_rate) :
        ult = UltraSensor.distance()
        if (diff(base, ult)) :
            client.publish(MQTT_Topic_Status,"T" + MQTT_ClientID)
        start = time.time()



