#coding:utf-8

#Params---------------------------------------------------------------

# query bit length
bit_length = 16

# LED光強度

r_intensity = 255
g_intensity = 255
b_intensity = 255

# LED array size
LED_array_length = 64

#prefix=01
##This time, Group_ID is static.
Group_ID = [0,1,0]

#Node_ID is varied according to Edge(IoT device)
Node_ID = [0,0,0]

prefix = Group_ID + Node_ID

# 点灯間隔
break_time = 5

# PCに返信するtopic先。デバイス番号に合わせて"topic{ デバイス番号 }_return"にする
topic_return = "topic1_return"

import paho.mqtt.client as mqtt
import time
from time import sleep
from datetime import datetime
import numpy as np
from sense_hat import SenseHat

#myfunction
import Encoder_myfunction

#Myfunc class
myfunc = Encoder_myfunction.MyClass()

#Sensehat class
sense = SenseHat()

# MQTT Broker
MQTT_HOST = "172.16.120.148"       # brokerのアドレス
MQTT_PORT = 1883                # brokerのport
MQTT_KEEP_ALIVE = 60            # keep alive

# broker接続時
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

#メッセージ受信時
def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    
    global query, on_message_Flag
    query = msg.payload.decode()
    
    # 受信すると状態はTrue
    on_message_Flag = True

mqttc = mqtt.Client()
mqttc.on_message = on_message  # メッセージ受信時に実行するコールバック関数設定
mqttc.on_connect = on_connect
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

mqttc.subscribe("topic1")  # Topic名："topic1"を購読


# 受信状態管理 初期設定
on_message_Flag = False

# 実行状態
run = True

# 受信回数
i = 0
while run: # topicを受け取ったらスタート
    # 割り込み処理
    mqttc.loop()  # 永久ループ
    if on_message_Flag: # 受信するとTrueになる
    
        i=i+1
        print("test:", i)
        
        # IoTセンシング & 符号化画像表示
        
        #coding: utf-8

        print("query:", query)

        # 撮影のため全点灯・全消灯
        print("DOC start")

        #------------------------------符号器検出(背景差分)
        e=[0,0,0]
        w=[255,200,180]
        z3 = [e]*64
        #z4 = [w]*64
        z4 = [
            w,w,w,w,w,w,w,w,
            w,w,w,e,e,w,w,w,
            w,w,e,w,e,w,w,w,
            w,w,w,w,e,w,w,w,
            w,w,w,w,e,w,w,w,
            w,w,w,w,e,w,w,w,
            w,w,e,e,e,e,w,w,
            w,w,w,w,w,w,w,w,
            ]

        #1
        #点灯
        sense.set_pixels(z4)
        time.sleep(break_time)
        sense.clear()

        #消灯
        time.sleep(break_time)



        #Params to be Encoded------------------------------------------------------------------------------------------------
    

        # time
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second

        ###environmental data
        #temperature
        temperature = int(sense.get_temperature())
        
        #pressure
        #only last 2 digits
        pressure = int(sense.get_pressure()) - 1000
        
        #humidity
        humidity = int(sense.get_humidity())

        ##data_edit-------------------------------------------------------------

        ###time
        hour_binary = myfunc.binary(hour, 6)
        minute_binary = myfunc.binary(minute, 6)
        second_binary = myfunc.binary(hour, 6)

        ###environmental data
        temper_binary = myfunc.binary(temperature, 8)
        press_binary = myfunc.binary(pressure, 8)
        humid_binary = myfunc.binary(humidity, 8)

        ##minute_binary is splited 4bit(Spectral B) and 2bit(Spectral R)
        minute_B = minute_binary[0:4:1]
        minute_G = minute_binary[4:6:1]

        # convert edited data to RGB_array----------------------------------------------------------------------------------------------------
        ##Spectral B
        B_array = prefix + hour_binary + minute_B
        ##Spectral G
        G_array = minute_G + second_binary + temper_binary
        ##Spectral R
        R_array = press_binary + humid_binary

        #query choice-----------------------------------------------------
        print("query:",query)

        #Queryで渡される値。Publisher側で指定している
        binary_query = [int(i) for i in query]
        # print("binary_query:",binary_query)

        com_key = binary_query*2
        print("com_key:",com_key)

        # spatial encode

        #R
        R_x, R_y = myfunc.input(com_key, R_array, bit_length)

        #G
        G_x, G_y = myfunc.input(com_key, G_array, bit_length)

        #B
        B_x, B_y = myfunc.input(com_key, B_array, bit_length)

        # spatial encode
        R = myfunc.spatial_encode(R_x, R_y, bit_length, r_intensity, LED_array_length)
        G = myfunc.spatial_encode(G_x, G_y, bit_length, g_intensity, LED_array_length)
        B = myfunc.spatial_encode(B_x, B_y, bit_length, b_intensity, LED_array_length)

        image_array = myfunc.set_array(R, G, B , LED_array_length)

        sense.set_pixels(image_array)
        time.sleep(break_time)
        sense.clear()
        
        # 送信するデバイス情報
        Device_info = ''.join(map(str, prefix[0:3])) + "/" + ''.join(map(str, prefix[3:6])) + "/" + str(hour) + ":" + str(minute) + ":" + str(second) + "/" + str(temperature) + "/" + str(pressure) +"/" + str(humidity)
        print(Device_info)
        # サーバに送信
        mqttc.publish(str(topic_return), Device_info)
        
        # 終了判定
        on_message_Flag = False
    
