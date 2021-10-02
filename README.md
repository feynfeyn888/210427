## 構成
```
Encoder:符号器(エッジデバイス)での実行フォルダ
Decoder:PC+カメラ(エッジゲートウェイ)での実行フォルダ
```

## Raspberry Pi 接続方法

```
ssh {user}@{IP address}
```

## 実行手順
```
# raspi
python topic_subscriber.py

# PC
conda activate DOCI
python3 main.py

# (option)PC
python topic_return.py
```
