import paho.mqtt.client as mqtt
from django.conf import settings
from random import uniform , randrange
import time

mqttBroker = "localhost"
client = mqtt.Client("Temprature_Inside")
client.connect(mqttBroker)

i = 0

while i<11:
    randNumber = uniform(20.0,21.0)
    client.publish("TEMPERATURE",randNumber)
    # print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
    i +=1


client.connect(settings.MQTT_BROKER_HOST, settings.MQTT_BROKER_PORT, 60)

client.loop_start()