#coding: utf-8

import numpy as np
#myfunc for encoder

class MyClass:

    def binary(self, input, digit):
        #input:str, digit:bit length
        binary = format(input, 'b')
        binary_array = [int(i) for i in binary]
        binary_array = [0]*(int(digit)-len(binary_array)) + binary_array

        return binary_array


    def query(self):
        #query choice
        s1 = list(msg.payload)
        print("s1(Query)",s1)

        #Query Value. Publisher側で指定
        a = [int(i) for i in s1]
        print("a",a)

    #----------------------------------------------------------------

    #a,b cahange into x,y--------------------------------------------
    def input(self, query, binary_array, bit_length):

        a = query
        b = binary_array

        #bit_length = 16
        length = bit_length
        
        a_ = np.zeros(length,dtype=np.int)
        b_ = np.zeros(length,dtype=np.int)
        x = np.zeros(length,dtype=np.int)
        y = np.zeros(length,dtype=np.int)

        #a_に変換.1と0を反転
        for i in range(length):
            if a[i]==0:
                a_[i]=1
            elif a[i]==1:
                a_[i]=0    

        #b_に変換
        for i in range(length):
            if b[i]==0:
                b_[i]=1
            elif b[i]==1:
                b_[i]=0 

        #x生成 (a*b)
        #np.logical_and(a,b):a and b と同じ。and演算。
        c = np.logical_and(a,b)

        #and演算の結果が1だったら1を返す
        for i in range(length):
            if c[i]==True:
                x[i]=1
            elif c[i]==False:
                x[i]=0

        #y生成 (a_*b)
        c = np.logical_and(a_,b)
        for i in range(length):
            if c[i]==True:
                y[i]=1
            elif c[i]==False:
                y[i]=0
        
        x = np.reshape(x,(1,length))
        y = np.reshape(y,(1,length))
        x = x[0].tolist()
        y = y[0].tolist()

        return x,y

    def spatial_encode(self, input_x, input_y, bit_length, intensity, LED_array_length):
       
        l=np.array([[0] for i in range(LED_array_length)])

        for i in range(bit_length):
            #LED上の配列
            index = i//4

            #左上
            if input_x[i]==0 and input_y[i]==0:
                l[2*i + index*8][0] = intensity

            #右上
            if input_x[i]==0 and input_y[i]==1:
                l[2*i + index*8+1][0] = intensity

            #左下
            if input_x[i]==1 and input_y[i]==0:
                l[2*i + index*8+8][0] = intensity

            #右下
            if input_x[i]==1 and input_y[i]==1:
                l[2*i + index*8+9][0] = intensity

        l = np.reshape(l,(1,LED_array_length)) 
        l = l[0].tolist()

        return l

    def set_array(self, R, G, B, LED_array_length):
        image_array = []

        for i in range(LED_array_length):
            image_array.append([R[i],G[i],B[i]])

        return image_array

