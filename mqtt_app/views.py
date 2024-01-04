from django.shortcuts import render
from .mqtt_handler import client


def my_view(request):
    # Your view logic here
    client.publish("your_topic", "Hello, MQTT!")
    return render(request, 'template.html')
