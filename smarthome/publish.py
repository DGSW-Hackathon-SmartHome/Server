from subscribe import on_connect
import paho.mqtt.client as mqtt
import json

class mqtt_publish():
    def __init__(self):
        self.mqtt = mqtt.Client()
        self.mqtt.connect('3.34.177.215', 1883)
        self.mqtt.loop_start()

    def temperature(cmd):
        if cmd == 'aircon_on':
            j = {
                "type": "aircon",
                "cmd": "on"
            }
            mqtt.publish("smarthome/sensor/temperature", json.dumps(j).encode())
        elif cmd == 'aircon_off':
            j = {
                "type": "aircon",
                "cmd": "off"
            }
            mqtt.publish("smarthome/sensor/temperature", json.dumps(j).encode())
        elif cmd == 'boiler_on':
            j = {
                "type": "boiler",
                "cmd": "on"
            }
            mqtt.publish("smarthome/sensor/temperature", json.dumps(j).encode())
        elif cmd == 'boiler_off':
            j = {
                "type": "boiler",
                "cmd": "off"
            }
            mqtt.publish("smarthome/sensor/temperature", json.dumps(j).encode())

    def humidity(cmd):
        if cmd == 'dehumidifier_on':
            j = {
                "type": "dehumidifier",
                "cmd": "on"
            }
            mqtt.publish("smarthome/sensor/humidity", json.dumps(j).encode())
        elif cmd == 'dehumidifier_off':
            j = {
                "type": "dehumidifier",
                "cmd": "off"
            }
            mqtt.publish("smarthome/sensor/humidity", json.dumps(j).encode())
        elif cmd == 'humidifier_on':
            j = {
                "type": "humidifier",
                "cmd": "on"
            }
            mqtt.publish("smarthome/sensor/humidity", json.dumps(j).encode())
        elif cmd == 'humidifier_off':
            j = {
                "type": "humidifier",
                "cmd": "off"
            }
            mqtt.publish("smarthome/sensor/humidity", json.dumps(j).encode())

    def air(cmd):
        if cmd == 'fan_on':
            j = {
                "type": "fan",
                "cmd": "on"
            }
            mqtt.publish("smarthome/sensor/air", json.dumps(j).encode())
        elif cmd == 'fan_off':
            j = {
                "type": "fan",
                "cmd": "off"
            }
            mqtt.publish("smarthome/sensor/air", json.dumps(j).encode())

    def gasvalve(cmd):
        if cmd == 'gasvalve_on':
            j = {
                "type": "gasvalve",
                "cmd": "on"
            }
            mqtt.publish("smarthome/gasValve", json.dumps(j).encode())
        elif cmd == 'gasvalve_off':
            j = {
                "type": "gasvalve",
                "cmd": "off"
            }
            mqtt.publish("smarthome/gasValve", json.dumps(j).encode())

    def led(cmd):
        if cmd == 'livingroom_led_on':
            j = {
                "type": "livingroom",
                "cmd": "on"
            }
            mqtt.publish("smarthome/sensor/led", json.dumps(j).encode())
        elif cmd == 'livingroom_led_off':
            j = {
                "type": "livingroom",
                "cmd": "off"
            }
            mqtt.publish("smarthome/sensor/led", json.dumps(j).encode())
        elif cmd == 'room_led_on':
            j = {
                "type": "room",
                "cmd": "on"
            }
            mqtt.publish("smarthome/sensor/led", json.dumps(j).encode())
        elif cmd == 'room_led_off':
            j = {
                "type": "room",
                "cmd": "off"
            }
            mqtt.publish("smarthome/sensor/led", json.dumps(j).encode())
        elif cmd == 'toilet_led_on':
            j = {
                "type": "toilet",
                "cmd": "on"
            }
            mqtt.publish("smarthome/sensor/led", json.dumps(j).encode())
        elif cmd == 'toilet_led_off':
            j = {
                "type": "toilet",
                "cmd": "off"
            }
            mqtt.publish("smarthome/sensor/led", json.dumps(j).encode())