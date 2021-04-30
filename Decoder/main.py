# python組み込み関数
import os
from time import sleep
import time
from datetime import datetime

# OpenCV
import cv2
import numpy as np

# pyueye関数
from module_.pyueye_example_camera import Camera
from pyueye import ueye


# MQTT通信
import paho.mqtt.client as mqtt  # ライブラリのimport
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

# 自作関数
from topic_publish import publish
from img_capture_pyueye import capture
from img_cutting import img_cutting
from DOC_masking import DOC_masking
from decode import decode

### params

# query
query = "10101001"

# 撮影露光時間(ms)
exposure_time = 50.0

# 撮影間隔(s)
break_time = 4

# path
relative_path =  os.getcwd()
# print(relative_path)


if __name__ == "__main__":
    
    # 基本的に変えなくてOK
    # MQTT Broker
    # MQTT_HOST : brokerのアドレス
    # MQTT_PORT : brokerのport
    # MQTT_KEEP_ALIVE : keep alive
    
    publish(MQTT_HOST="172.16.120.148", MQTT_PORT=1883, MQTT_KEEP_ALIVE=60, query=query)
    print("query:", query)
    
    print("publish")

    # 撮影開始
    print("\n撮影開始")
    # 引数1:id, 引数2:撮影間隔, 引数3:露光時間(ms), 引数4:相対パス
    for i in range(3):
        capture(device_id=i, break_time=break_time, exposure_time=exposure_time, relative_path=relative_path)
        
    # 符号化画像切り出し
    print("\n切り出し開始")
    detect_number = img_cutting(relative_path=relative_path)

    # マスキング
    print("\nマスキング開始")
    # k:符号器の数, relative_path:相対パス, thre:閾値
    DOC_masking(k=5, relative_path=relative_path, thre=90)
    
    # k:符号器の数
    print("\n")
    print("復号開始")
    decode(k=5, relative_path=relative_path)
