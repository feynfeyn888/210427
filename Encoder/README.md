## Quick Start
```Encoder/topic_subscribe.py```を実行する(python3であることを確認の上、実行)

## IP address

### Broker
```172.16.120.148```

### Edge Device
```
Device 1:172.16.120.228
Device 2:172.16.120.121
Device 3:172.16.120.149
Device 4:172.16.120.159
Device 5:172.16.120.
```

## 実行内容について
1. topic_subscribe.pyを実行すると, topicを受信待機するようになる。
2. topicを受信すると、背景差分法によるデバイス検出を行うため、全点灯・全消灯・符号化画像表示を行う
3. 各デバイスは、```topic{device_id}```のtopicに送られてきたQuery(データ)から、以下の符号化規約でを符号化する
```
###Code Assignment
---Spectral B channel---
Group ID (3bit) [g2g1g0]
Node ID (3bit) [i2i1i0]
Time_1 (10bit(6bit,4bit)) [h5h4h3h2h1h0][m5m4m3m2]
---Spectral G channel---
Time_2 (8bit) [m1m0][s5s4s3s2s1s0]
Temperature (8bit) [a5a4a3a2a1a0]
---Spectra R channel---
Atmospheric Pressure (8bit) [b5b4b3b2b1b0]
Humidity (8bit) [c5c4c3c2c1c0]
###Data Format and Prefixed Values
Encryption Common Key:  10101101
Group ID:  010
Node ID:    000, 001, 010, 011, 100
Time: (0〜23 : 0〜59 : 0〜59)   [h5h4h3h2h1h0][m5m4m3m2m1m0][s5s4s3s2s1s0]
Temperature: (0〜100) [deg]    [a5a4a3a2a1a0]
Atmospheric pressure: (0〜100)[%][hPa]     [b5b4b3b2b1b0]
Humidity: (0〜100)[%]  [c5c4c3c2c1c0]
```
4. RGBそれぞれに符号化画像を表示したのち、```topic{ device_id }_return```にセンサ情報を送信する。センサ情報の割り当ては以下の通り。

```Group_ID/Device_ID/hour:minute:second/温度/圧力/湿度 ```


## raspberry pi IPアドレス固定化
1. Wi-fiのアイコンを右クリック、Wireless&Wired Network Settingsを開く
2. interface->wlan0にしたのち、以下のように設定する
```
IPv4 Address:172.16.120.{2~254の間で設定}
Router:172.16.120.254
DNS Servers: 133.1.173.70
