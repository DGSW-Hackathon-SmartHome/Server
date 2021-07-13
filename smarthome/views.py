
from smarthome.subscribe import mqtt_subscribe
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt    # csrf 비활성화 라이브러리
from django.utils.decorators import method_decorator    # csrf 비활성화를 위한 메서드, 클래스 데코레이터

@method_decorator(csrf_exempt, name='dispatch')
def getAllSensor(request):
    json = mqtt_subscribe()
    return render(request, 'index.html', json)

@method_decorator(csrf_exempt, name='dispath')
def control_temp(request):
    json = mqtt_subscribe()
    if request.method == "POST":
        return redirect(control_temp)

    return render(request, 'temp.html', json)
