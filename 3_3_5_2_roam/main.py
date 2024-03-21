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
MQTT_ClientID = 'obo'
MQTT_Broker = '192.168.4.244'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


bob = DriveBase(left_motor, right_motor, wheel_diameter = 54, axle_track = 105)
s = bob.settings()
bob.settings(200,200,s[2],s[3])


def listen(topic, msg) :
    pass

# List for the way
count = [0]

# Write your program here.
client.connect()
time.sleep(0.5)
ev3.screen.print('Started')
client.set_callback(listen) 
client.subscribe(MQTT_Topic_Status) 
time.sleep(0.5)
ev3.screen.print('Listening')

TSensor = TouchSensor(Port.S1)
UltraSensor = UltrasonicSensor(Port.S4)

bob.drive(200,0)
flag = [True]
while (not TSensor.pressed()) :
    if (flag[0] and count[0] == 10) :
        bob.stop()
        ev3.light.on(Color.RED)
        client.publish(MQTT_Topic_Status, MQTT_ClientID + " is stopped")
        flag[0] = False
    if (flag[0] and UltraSensor.distance() < 300) :
        bob.turn(45)
        bob.drive(200,0)
        count[0] += 1
        print(count)

