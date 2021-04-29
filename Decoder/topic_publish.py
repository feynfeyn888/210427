
import paho.mqtt.client as mqtt  # ライブラリのimport
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
from time import sleep
import time
from datetime import datetime

# -*- coding: utf-8 -*-

# broker接続時
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))             # 接続結果表示

def publish(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE, query):
    mqttc = mqtt.Client()    #clientオブジェクト作成
    mqttc.on_connect = on_connect  # 接続時に実行するコールバック関数設定

    mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)  # MQTT broker接続

    mqttc.loop_start() # 処理開始

    mqttc.publish("topic1", query)  # topic名="Topic1"に "test1"というメッセージを送信
    mqttc.publish("topic2", query)
    mqttc.publish("topic3", query)
    mqttc.publish("topic4", query)
    mqttc.publish("topic5", query)

if __name__ == "__main__":
    
    query = "10101001"
    print("query:", query)
    
    publish(MQTT_HOST="172.16.120.148", MQTT_PORT=1883, MQTT_KEEP_ALIVE=60, query=query)
    print("publish")

