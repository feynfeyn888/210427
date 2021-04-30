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
sshで各ラズパイの送受信実行ファイルtopic_subscriber.pyを起動したのち、PCでmain.pyを実行する.

PCで各符号器のセンサデータを取得する場合はtopic_return.pyも実行する.
```

詳細は各フォルダ```README.md```参照

## 注意点

### 画像切り出しについて
```
OpenCVで背景差分法を用いて画像を切り出すとき, 画像が回転されて切り出されることが頻発する.
原因について詳細に調べたわけではないが, 符号器をカメラに正対させた後、少し左に傾けると回避できるので, 画像を切り出す際の座標が関与していると思われる.
```

### 画像の復号について
```
既存の画像ファイルを読み込んで復号処理を行うため, 撮影がうまくいっていなくても復号処理は進むことに注意.
うまくいっていない場合は, image_thre.pngを確認して、きちんと切り出しが行えているか確認する.
```

### 波長多重について
```
バンドパスフィルタでやってみたところ、光量が足りず符号化画像の抽出がうまくいかなかった。
露光時間を増やす等が必要になりそう。
符号器の表示も疑似的に多重化することを検討
```

## 開発環境
```
PC:VSCode
ラズパイ:Python IDE or PCからssh接続してVimでファイル編集を行う
```

## ソースファイルの印刷
GitHub上でファイルを開き、```Raw```をクリックして印刷.
