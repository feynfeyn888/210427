#!/usr/bin/env python
#coding:utf-8

import cv2
import numpy as np
import os

################################

# k:符号器の数, relative_path:相対パス
def DOC_masking(k, relative_path, thre):
    for iter in range(k):#符号器の数繰り返す
    #画像の読み出し
        index = iter + 1
        # 各画像を読みだしていく
        img = cv2.imread(relative_path + "/img/cutting/"+str(index)+"/encode_image_encoder_id_"+str(index)+".png",0)
        
        # 画像ファイルが空かどうか判定
        if img is None:
            print("画像ファイルが空です")
            print(str(iter)+"台分の符号器を検出しました")
            break
        
        # 画像サイズ確認
        # height, width = img.shape[:2]
        # print(height, width)
    
        # 切り出し間隔 = 切り出し画像/10
        cutting_pitch = 20

        # 画像の重ね合わせ
        w=int(img.shape[0]/8)#img.shape[0]:画像の縦列
        h=int(img.shape[1]/8)#img.shape[1]:画像の横列

        img1 = img[w:8*w,h:8*h]#右下切り取り　1LED左上　
        img2 = img[w:8*w,0:7*h]#左下切り取り　1LED左
        img3 = img[0:7*w,h:8*h]#右上切り取り　1LED上
        img4 = img[0:7*w,0:7*h]#左上切り取り　これを基本とする
        
        #XORはimg2とimg3を選択
        imgc1 = img2#[左下7*7画像]
        imgc2 = img3#[右上7*7画像]
        img_weighted = cv2.addWeighted(imgc1, 0.5, imgc2, 0.5, 0)
        img = np.array(img_weighted)
        for i in range(int(3)):#横縞#3回
            cv2.rectangle(img, (0, h*(2*i+1)), (8*h, h*(2*i+2)), (0, 0, 0), thickness=-1)
        for j in range(int(3)):#縦縞
            cv2.rectangle(img, (w*(2*j+1), 0), (w*(2*j+2), 8*w), (0, 0, 0), thickness=-1)
        cv2.imwrite(relative_path + "/img/cutting/"+str(index)+"/decode/decode_mask_"+str(index)+".png", img)

        # 画像の切り出し
        for delete in range(3):
            #8画素ずつマスクをしたところを切り出していく
            img = np.delete(img,np.s_[cutting_pitch*(delete+1):cutting_pitch*(delete+1)+cutting_pitch], axis=0) #列(要素)の消去
            # img = np.delete(img,np.s_[0*w:8*w:3*w], axis=0)
            img = np.delete(img,np.s_[cutting_pitch*(delete+1):cutting_pitch*(delete+1)+cutting_pitch], axis=1) #行の消去
            # img = np.delete(img,np.s_[0*w:8*w:3*w], axis=1)

        ret, img = cv2.threshold(img, thre, 255, cv2.THRESH_BINARY)
        #閾値を100にしている。ノイズが多い場合は変更する必要あり。
        cv2.imwrite(relative_path +"/img/cutting/"+str(index)+"/decode/DOC_decode_" + str(index) +".png", img)
        cv2.imwrite(relative_path +"/DOC_output/DOC_decode_" + str(index) +".png", img)

if __name__ == "__main__":
    # 相対パス取得
    relative_path =  os.getcwd()

    # 閾値(defalut)
    thre = 90
    
    # k:符号器の数, relative_path:相対パス, thre:閾値
    DOC_masking(k=5, relative_path=relative_path, thre=90)