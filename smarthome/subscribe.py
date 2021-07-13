import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connect")
    client.subscribe('smarthome/value')

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    j = json.loads(msg.payload)
    if msg.topic == 'smartfarm/value':
        return j
        if j['temperature']:       # 온도 값
            pass
        elif j['aircon']:          # 에어컨 on/off
            pass
        elif j['boiler']:          # 보일러 on/off
            pass
        elif j['humidity']:        # 습도 값
            pass
        elif j['humidifier']:      # 가습기 on/off
            pass
        elif j['dehumidifier']:    # 제습기 on/off
            pass
        elif j['air']:             # 미세먼지 값
            pass
        elif j['fan']:             # 환풍기 on/off
            pass
        elif j['gasvalve']:        # 가스밸브 on/off
            pass
        elif j['led']:              
            if['livingroom']:      # 거실 led on/off
                pass
            elif['room']:          # 방 led on/off
                pass
            elif['toilet']:        # 화장실 led on/off
                pass

class mqtt_subscribe():
    def __init__(self):
        self.client = mqtt.Client
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.connect("3.34.177.215", 1883)
        self.client.loop_forever()