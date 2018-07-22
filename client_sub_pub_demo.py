#!/usr/bin/python
# -*- coding: utf-8 -*-
# 本例程用paho.mqtt.client类，进行完整的 连接-维持-订阅-发布-断开 操作.
'''
对于简单应用，直接发一包信息到broker后立即断开连接，可用paho.mqtt.publish类
publish.single(topic, payload=None, qos=0, retain=False, hostname="localhost",    port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None,    protocol=mqtt.MQTTv311, transport="tcp")
'''
'''
对于简单应用，订阅信息后打印，可用paho.mqtt.subscribe类，例如：
import paho.mqtt.subscribe as subscribe
msg = subscribe.simple("paho/test/simple", hostname="iot.eclipse.org")
print("%s %s" % (msg.topic, msg.payload))
'''

import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
import time
import random

def on_connect(mqttc, obj, flags, rc):
    print("result of connect: " + str(rc))

def on_message(mqttc, obj, msg):
    print("Topic: "+msg.topic + " -- QOS:" + str(msg.qos) + " -- payload:" + str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("message Id: " + str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

#prototype: connect(host, port=1883, keepalive=60, bind_address="")
mqttc.connect("gariel.top", 1883, 60)

mqttc.loop_start()

#prototype: subscribe(topic, qos=0)
mqttc.subscribe("#", 0)

a=b=c=0
d=e=100
while True:
    a=a+1
    b=random.randrange(0,100,1)
    c=a+b
    d=d-1
    e=d*d
    #prototype: publish(topic, payload=None, qos=0, retain=False)
    mqttc.publish("m1/sig_a", a)
    mqttc.publish("m1/sig_b", b)
    mqttc.publish("m1/sig_c", c)
    mqttc.publish("m1/sig_d", d)
    mqttc.publish("m1/sig_e", e)

    time.sleep(2)
    if a>=100:
        a=0
    if d<=0:
        d=100

mqttc.loop_stop()

#mqttc.loop_forever()
