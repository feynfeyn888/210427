# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import time

# S1:172.16.120.55
# S2:172.16.120.56
# S3:172.16.120.57
# S4:172.16.120.59
# S5:172.16.120.52
# Broker:172.16.120.63


# MQTT Broker
MQTT_HOST = "172.16.120.63"       # brokerのアドレス
MQTT_PORT = 1883                # brokerのport
MQTT_KEEP_ALIVE = 60            # keep alive

# broker接続時
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

#メッセージ受信時
def on_message(mqttc, obj, msg):
    global on_message_Flag         # メインループと共有するグローバル変数
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    on_message_Flag=True          # flagを有効化

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

mqttc.subscribe("topic1_return")
mqttc.subscribe("topic2_return")
mqttc.subscribe("topic3_return")
mqttc.subscribe("topic4_return")
mqttc.subscribe("topic5_return")

while True:
    mqttc.loop_start()
