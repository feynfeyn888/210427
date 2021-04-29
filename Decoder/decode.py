#!/usr/bin/env python
#coding:utf-8

import os
import cv2
import numpy as np

def decode(k, relative_path):
    # テキストファイル作成
    path = relative_path + "/DOC_output/output.txt"
    with open(path, mode="w", encoding="utf-8") as f:
        f.write("復号結果")
        
    for iter in range(k):#符号器の数繰り返す
    #画像の読み出し
        # 各画像を読みだしていく
        img = cv2.imread(relative_path + "/DOC_output/DOC_decode_" + str(iter+1) + ".png",0)
        
        # 画像ファイルが空かどうか判定
        if img is None:
            print(str(iter)+"台復号")
            print("end")
            break
        
        # 復号を行っていく
        output = []
        for i in range(4):
            for j in range(4):
                mean=np.mean(img[8*i:8*(i+1)-1, 8*j:8*(j+1)-1])
                if mean<50:
                    mean=0
                    output.append(mean)
                else:
                    mean=1
                    output.append(mean)
        print("output"+str(iter+1)+"台目:", output)
        with open(path, mode="w", encoding="utf-8") as f:
            f.write(str(iter+1)+"台目:"+str(output)+"\n")
    
    # 
if __name__ == "__main__":
    ### params ###
    ## 符号器の数に合わせる
    k = 5
    # 相対パス
    relative_path =  os.getcwd()
    print(relative_path)
    
    # k:符号器の数
    decode(k=5, relative_path=relative_path)