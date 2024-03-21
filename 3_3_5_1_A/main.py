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
MQTT_Broker = '192.168.16.244'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# Create your objects here.
ev3 = EV3Brick()
robot_id = 'A'

plays = ["A", "B", "C"]
song = "C,2,D,4,E,4,F,2,G,4,A,4,B,2,C,4"
BPM = 120
done = [False]


def listen(topic,msg) :
    if topic == MQTT_Topic_Status.encode() :
        data = str(msg.decode())
        ev3.screen.print(data)
        if (data[0] in plays) :
            done[0] = False
            beep([data])
        if (data == "Z") :
            done[0] = True

def beep(note) :
    ev3.speaker.play_notes(note, BPM)
    done[0] = True

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
                s+= '2/'
            i += 1
        else :
            s += t
            i += 1
    L.append(s)
    return L

def send(data) :
    done[0] = False
    client.publish(MQTT_Topic_Status,data)
    while(not done[0]) :
        client.check_msg()

# Write your program here.
client.connect()
time.sleep(0.5)
ev3.screen.print("Connected")
client.set_callback(listen) 
client.subscribe(MQTT_Topic_Status) 
time.sleep(0.5)
ev3.screen.print("Listenning...")

start = time.time()
tick = 0.5

S = convert(song)
l = len(S)
i = 0

while (True) :
    client.check_msg()
    if (time.time() - tick >= start and i < l) :
        start = time.time()
        send(S[i])
        i += 1