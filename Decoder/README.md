## Quick Start

```
1. VSCodeを起動. ターミナルから、
    $conda activate DOCI
   で実行環境を起動する
2. ssh接続などでEncoder(ラズパイ)のtopic_subscriber.pyを実行し, 受信可能な状態にする
3. topic_return.pyを実行. 符号器で送信したデータをPCで受信できるようになる
4. main.pyを実行.
5. output.txtにバイナリにて復号結果が表示される
```

## センサ情報の取得
topic_return.pyを実行していれば、各デバイスが符号化した情報を受信できる.

## ディレクトリ構成
```
C:.
│  decode.py # 復号処理実行ファイル 
│  DOC_masking.py # mask実行
│  img_capture_pyueye.py # 撮影
│  img_cutting.py # 符号化画像切り出し
│  main.py # 実行ファイル
│  pyueye_example_utils.py # pyueye設定ファイル
│  README.md
│  topic_publish.py # topic送信
│  topic_return.py # topic受信
│
|  DOCI.yml # 仮想環境ファイル
|
├─DOC_output # DOC結果
│      DOC_decode_1.png # 復号画像
│      output.txt # 復号結果表示
│
├─img
│  │  DOC_0.png # 全点灯
│  │  DOC_1.png # 全消灯
│  │  DOC_2.png # 符号化画像表示
│  │
│  ├─cutting # 切り出し画像フォルダ
│  │  ├─1 # 切り出し番号(Device番号と非対応)
│  │  │  │  encode_image_encoder_id_1.png # 符号化画像
│  │  │  │
│  │  │  └─decode
│  │  │          decode_mask_1.png # マスク画像
│  │  │          DOC_decode_1.png # 復号画像
│  │  │
│  │  ├─2
│  │  ├─3
│  │  ├─4
│  │  └─5
│  └─post # 符号化画像切り出し精度の確認用
│          image_abs_gray.png
│          image_capture_binary.png
│          image_contours.png
│          image_thre.png # 符号化画像をうまく切り出せているか確認. うまく復号ができない場合は切り出しがうまくいっていない可能性が高いので確認する.
│
└─module_　# pyueye用モジュール
```
