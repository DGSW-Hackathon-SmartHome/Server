from django.shortcuts import redirect, render

def getAllSensor(request):
    returnValue = {
        "gas": {
            "status": 0,  # -1: 부족함, 0: 적당함, 1: 많음
            "value": 12,
        },
        "temperature": {
            "status": 0,
            "value": 48,
        },
        "humidity": {
            "status": 0,
            "value": 24,
        },
        "led": {
            "onoff": "ON or OFF",  # 0: 꺼짐, 1: 켜짐
        },
        "fan": {
            "onoff": "ON or OFF",  # 0: 꺼짐, 1: 켜짐
        },
    }

    return render(request, 'index.html', returnValue)

def gasPost(request):
    if request.method == "POST":
        some_var = request.POST.getlist('gasOnOff[]')
        content = {
            "onOff": some_var,
            "ONOFF": "on",
        }
    return redirect('main/')