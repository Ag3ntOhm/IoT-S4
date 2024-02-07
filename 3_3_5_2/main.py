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
MQTT_ClientID = 'bob'
MQTT_Broker = '192.168.49.231'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


bob = DriveBase(left_motor, right_motor, wheel_diameter = 54, axle_track = 105)
s = bob.settings()
bob.settings(200,200,s[2],s[3])

# List for the way
L = []


def RepWay() :
    for inst in L :
        if (inst[0] == 'S') :
            bob.straight(int(inst[1:]))
        if (inst[0] == 'T') : 
            bob.turn(int(inst[1:]))


def Store(msg) :
    print(msg)
    if (msg == "AF") :
        RepWay()
        return
    if (msg[0] == "B") : 
        return
    L.append(msg[1:])

def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        Store(msg.decode())

# Write your program here.
client.connect()
time.sleep(0.5)
ev3.screen.print('Started')
client.set_callback(listen) 
client.subscribe(MQTT_Topic_Status) 
time.sleep(0.5)
ev3.screen.print('Listening')



while True :
    client.check_msg()
    time.sleep(0.5)


