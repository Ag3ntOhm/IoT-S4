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
MQTT_Broker = '192.168.110.244'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# Create your objects here.
ev3 = EV3Brick()
robot_id = 'A'

listA = []
listB = ["F", "G", "B", "A"]

song = "C,2,D,4,E,4,F,2,G,4,A,4,B,2,C,4"
BPM = 120
# func

def listen(topic, msg) :
    if topic == MQTT_Topic_Status.encode() :
        data = str(msg.decode())
        ev3.screen.print(data)
        if (data[0] == robot_id) :
            beep([data[1:]])

def beep(note) :
    ev3.speaker.play_notes(note, BPM)

def convert(Song) :
    L = []
    s = ""
    i = 0
    while i < len(Song) :
        if (i != 0 and i % 4 == 0) :
            L.append(s)
            s = ""
        t = Song[i]
        if (t == ',') :
            if (i % 2 != 1) :
                raise SyntaxError("Song invalid syntax")
            if (len(s) == 1) :
                s+= '/'
            i += 1
        else :
            s += Song[i]
            i += 1
    return L

def sorting(L) :
    T = []
    for i in range(len(L)) :
        if L[i][0] in listA :
            T.append(('A',L[i]))
        else :
            T.append(('B',L[i]))
    return T


# Write your program here.
client.connect()
time.sleep(0.5)
ev3.screen.print("Connected")
client.set_callback(listen) 
#client.subscribe(MQTT_Topic_Status) 
time.sleep(0.5)
ev3.screen.print("Listenning...")


if (robot_id == 'A') :
    print("in")
    L = convert(song)
    T = sorting(L)
    for i in T :
        print(i[0] + " " + i[1])
    for i in range(len(T)) :
        client.publish(MQTT_Topic_Status, T[i][0] + T[i][1])
        time.sleep(0.5)
else :
    while True :
        client.check_msg()
        time.sleep(0.1)