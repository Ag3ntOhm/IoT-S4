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


def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        code = str(msg.decode())
        if (code[0] == 'B') :
            ev3.screen.print(code[1:])

def control(topic, msg) :
    if topic == MQTT_Topic_Status.encode():
        code = str(msg.decode())
        if (code == 'Center button') :
            bob.stop()
        if (code == 'Right button') :
            bob.turn(45)
        if (code == 'Left button') :
            bob.turn(-45)
        if (code == 'Up button') :
            bob.drive(200,0)
        if (code == 'Down button') :
            bob.drive(-200,0)


def check_butt(b) :
    butt = ev3.buttons.pressed()
    if (butt != None and len(butt) != 0) :
        if b != None and b[0] == butt[0] :
            return None
        if (butt[0] == Button.CENTER) :
            client.publish(MQTT_Topic_Status, 'Center button')
            print("c")
        if (butt[0] == Button.RIGHT) :
            client.publish(MQTT_Topic_Status, 'Right button')
        if (butt[0] == Button.LEFT) :
            client.publish(MQTT_Topic_Status, 'Left button')
        if (butt[0] == Button.UP) :
            client.publish(MQTT_Topic_Status, 'Up button')
        if (butt[0] == Button.DOWN) :
            client.publish(MQTT_Topic_Status, 'Down button')
        return butt


# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

bob = DriveBase(left_motor, right_motor, wheel_diameter = 54, axle_track = 121)
# Write your program here.

client.connect()
time.sleep(0.5)
client.publish(MQTT_Topic_Status, 'Started')
ev3.screen.print('Started')
client.set_callback(control) 
client.subscribe(MQTT_Topic_Status) 
time.sleep(0.5)
client.publish(MQTT_Topic_Status, 'Listening')
ev3.screen.print('Listening')

UltraSensor = UltrasonicSensor(Port.S4)

butt = None
start = time.time()
while True:
    client.check_msg()
    #butt = check_butt(butt)
    if (time.time() - start > 1) :
        client.publish(MQTT_Topic_Status, "B" + str(UltraSensor.distance()))
        start = time.time()
    
