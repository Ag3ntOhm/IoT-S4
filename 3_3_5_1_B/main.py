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
MQTT_Broker = '192.168.16.244'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# Create your objects here.
ev3 = EV3Brick()
robot_id = 'B'

plays = ["D", "E", "F", "G"]
BPM = 120

def listen(topic,msg) :
    if topic == MQTT_Topic_Status.encode() :
        data = str(msg.decode())
        ev3.screen.print(data)
        if (data[0] in plays) :
            beep([data])

def beep(note) :
    ev3.speaker.play_notes(note, BPM)
    client.publish(MQTT_Topic_Status, "Z")


# Write your program here.
client.connect()
time.sleep(0.5)
ev3.screen.print("Connected")
client.set_callback(listen) 
client.subscribe(MQTT_Topic_Status) 
time.sleep(0.5)
ev3.screen.print("Listenning...")

while (True) :
    client.check_msg()