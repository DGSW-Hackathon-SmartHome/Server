import time
import paho.mqtt.client as paho
import json

broker = '3.34.177.215'

#define callback
def on_message(client, userdata, message):
    global recvData

    time.sleep(1)
    recvData = json.loads(message.payload)

client = paho.Client()
client.on_message = on_message

print("connecting to broker ", broker)
client.connect('3.34.177.215', 1883)
print("subscribing ")
client.subscribe("smarthome/value")#subscribe
client.loop_start() #start loop to process received messages
time.sleep(5)

def returnData():
    return recvData
print(recvData)