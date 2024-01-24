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
MQTT_ClientID = 'testmqtt'
MQTT_Broker = '192.168.49.231'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


bob = DriveBase(left_motor, right_motor, wheel_diameter = 54, axle_track = 121)

# Write your program here.
L = [261.63,293.66,329.63,349.23,392,440,493.88,523.25]

def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))
        bob.drive(200,0)
        ev3.speaker.play_notes(["F2/1"])
        time.sleep(1.5)
        bob.turn(160)
        bob.stop()

def play_song() :
    for i in L :
        ev3.speaker.beep(frequency=i,duration=200)

client.connect()
time.sleep(0.5)
#client.publish(MQTT_Topic_Status, 'Started')
ev3.screen.print('Started')
client.set_callback(listen) 
client.subscribe(MQTT_Topic_Status) 
time.sleep(0.5)
#client.publish(MQTT_Topic_Status, 'Listening')
ev3.screen.print('Listening')

while True:
    client.check_msg()
    time.sleep(0.5)
    
