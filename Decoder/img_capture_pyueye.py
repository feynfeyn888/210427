#!/usr/bin/env python
#coding:utf-8

from module_.pyueye_example_camera import Camera
from pyueye import ueye
from time import sleep
import time
from datetime import datetime
import os

#カメラ関数(pyueye_example_camera.py参照)
# 引数1:device_id, 引数2:撮影間隔(s), 引数3:露光時間(ms), 引数4:相対パス
def capture(device_id, break_time, exposure_time, relative_path):
    # camera class to simplify uEye API access
    file_name = relative_path + "/img/DOC_"+str(device_id)+".png"
    cam = Camera()
    cam.init()
    cam.set_colormode(ueye.IS_CM_BGR8_PACKED)
    cam.set_aoi(0,0, 2500, 2500)
    cam.alloc()
    #print(ueye.is_GetImageMem(self.h_cam,buff.mem_ptr))
    cam.set_pixelclock()
    cam.set_framerate()
    # 露光時間(ms)
    # 実験条件に合わせる
    cam.set_exposure(exposure_time)
    cam.capture_video()
    time.sleep(0.5)
    cam.image_file(file_name)
    cam.stop_video()
    cam.exit()

    print(datetime.now())
    print("capture")
    time.sleep(break_time)


if __name__ == "__main__":
    # path
    relative_path =  os.getcwd()
    # print(relative_path)
    
    # 引数1:device_id, 引数2:撮影間隔(s), 引数3:露光時間(ms), 引数4:相対パス
    for i in range(3):
        capture(device_id=i, break_time=4, exposure_time=50.0, relative_path=relative_path)