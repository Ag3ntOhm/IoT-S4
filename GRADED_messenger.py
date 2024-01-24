import paho.mqtt.client as mqtt
import tkinter as tk

#MQTT_BROKER = "broker.hivemq.com"
MQTT_BROKER = "mqtt.eclipseprojects.io"
#MQTT_BROKER = "192.168.218.115"
MQQT_TOPIC = "python/course"
DISPLAYED_MESSAGES = 12

# create MQTT client
client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQQT_TOPIC)

# connect callback functions
client.on_connect = on_connect

# main window
class App(tk.Tk):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.title("My Messenger")
        self.geometry("350x300")
        
# textfield & button for sending
class SendFrame(tk.Frame):

    # method to send a message
    def on_send(self):
        client.publish(MQQT_TOPIC, self.text.get())
        self.text.set("")

    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.text = tk.StringVar()
        tk.Entry(self, textvariable= self.text, width=30).grid(column=0, row=0)
        tk.Button(self, text = "send!", command= self.on_send).grid(column=1, row=0)
        tk.Button(self, text = "→").grid(column=2, row=0)

# the list of messages
class MessageFrame(tk.Frame):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.messages = []
        for i in range(DISPLAYED_MESSAGES):
            self.messages.append( tk.StringVar(self) )
            tk.Label(self, textvariable= self.messages[i]).pack()

    # method to update the Message list with received messages
    def add_message(self, msg):
        for i in range(DISPLAYED_MESSAGES-1):
            self.messages[i].set( self.messages[i+1].get() )
        self.messages[DISPLAYED_MESSAGES-1].set(msg)

app = App()
msg_frm = MessageFrame(app)
msg_frm.pack()
SendFrame(app).pack()

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if(msg.topic == MQQT_TOPIC):
        msg_frm.add_message( msg.payload.decode() )

# connect callback
client.on_message = on_message

client.loop_start()
app.mainloop()
client.loop_stop()
client.disconnect()