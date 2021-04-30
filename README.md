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
sshで各ラズパイの送受信実行ファイルを起動したのち、PCでmain.pyを実行する.

詳細は各フォルダ```README.md```参照

## 注意点

### 画像切り出しについて
```
OpenCVで背景差分法を用いて画像を切り出すとき、画像が回転されて切り出されることが頻発する.
原因について詳細に調べたわけではないが、符号器をカメラに正対させた後、少し左に傾けると回避できるので、画像を切り出す際の座標が関与していると思われる
```

### 波長多重について
```
バンドパスフィルタでやってみたところ、光量が足りず符号化画像の抽出がうまくいかなかった。露光時間を増やす等が必要になりそう
```

## 開発環境
```
PC:VSCode
ラズパイ:Python IDE or PCからssh接続してVimでファイル編集を行う
```
