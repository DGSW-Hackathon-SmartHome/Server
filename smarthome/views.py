
from smarthome import subscribe
import time
import json
import paho.mqtt.client as paho
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt    # csrf 비활성화 라이브러리
from django.utils.decorators import method_decorator    # csrf 비활성화를 위한 메서드, 클래스 데코레이터

broker = '3.34.177.215'

mqtt = paho.Client()
mqtt.connect(broker, 1883)
mqtt.loop(2)

@method_decorator(csrf_exempt, name='dispatch')
def getAllSensor(request):
    broker = '3.34.177.215'

    client = paho.Client()
    client.on_message=subscribe.on_message

    print("connecting to broker ", broker)
    client.connect(broker, 1883)
    print("subscribing ")
    client.subscribe("smarthome/value")#subscribe
    client.loop_start() #start loop to process received messages
    time.sleep(2)

    value = subscribe.returnData()

    return render(request, 'index.html', value)

@method_decorator(csrf_exempt, name='dispath')
def control_temp(request):
    if request.method == "GET":
        broker = '3.34.177.215'

        client = paho.Client()
        client.on_message=subscribe.on_message

        print("connecting to broker ", broker)
        client.connect(broker, 1883)
        print("subscribing ")
        client.subscribe("smarthome/value")#subscribe
        client.loop_start() #start loop to process received messages
        time.sleep(2)

        value = subscribe.returnData()

        return render(request, 'temp.html', value)

    elif request.method == "POST":
        control_aircon = request.POST['aircon_mode']
        # control_boiler = request.POST['boiler_mode']  

        if control_aircon == "ON":

            j = {
                "type": "aircon",
                "cmd": "off"
            }
            mqtt.publish("smarthome/sensor/temperature", json.dumps(j).encode())
        elif control_aircon == "OFF":
            j = {
                "type": "aircon",
                "cmd": "on" 
            }
            mqtt.publish("smarthome/sensor/temperature", json.dumps(j).encode())


        # 시간 관계상 작성하지 못한 코드
        # if control_boiler == "ON":
        #     j = {
        #         "type": "boiler",
        #         "cmd": "off",
        #     }
        #     mqtt.publish("smarthome/sensor/temperature", json.dumps(j).encode())
        # elif control_boiler == "OFF":
        #     j = {
        #         "type": "boiler",
        #         "cmd": "on",
        #     }
        #     mqtt.publish("smarthome/sensor/temperature", json.dumps(j).encode())

        return redirect(control_temp)

@method_decorator(csrf_exempt, name='dispath')
def control_humidity(request):
    broker = '3.34.177.215'

    client = paho.Client()
    client.on_message=subscribe.on_message

    print("connecting to broker ", broker)
    client.connect(broker, 1883)
    print("subscribing ")
    client.subscribe("smarthome/value")#subscribe
    client.loop_start() #start loop to process received messages
    time.sleep(2)

    value = subscribe.returnData()

    return render(request, 'humidity.html', value)

@method_decorator(csrf_exempt, name='dispath')
def control_led(request):
    broker = '3.34.177.215'

    client = paho.Client()
    client.on_message=subscribe.on_message

    print("connecting to broker ", broker)
    client.connect(broker, 1883)
    print("subscribing ")
    client.subscribe("smarthome/value")#subscribe
    client.loop_start() #start loop to process received messages
    time.sleep(2)

    value = subscribe.returnData()

    return render(request, 'led.html', value)