# pi_cv

Raspiで画像処理を行うサンプル集


## install

- 必要なモジュールをインストール

```sh
$ sudo apt-get update -y
$ sudo apt-get install python3-numpy -y
$ sudo apt-get install python3-matplotlib -y
$ sudo apt-get install libopencv-dev -y
$ sudo apt-get install python3-opencv -y
```

- git cloneで任意のディレクトリへクローンしてくる

```sh
$ git clone https://github.com/ynct-uchida-lab/pi_cv.git
```

## Usage

- ディレクトリ構造は以下の通り

```
.
└pi_cv
    ├data
    ├output
    └samples
        ├01_web_cam_show.py
        ├02_color_convert.py
        ├03_back_diff.py
        ├04_mask.py
        └05_dilate_erode.py
```

- data
    - 入力画像が格納
- output
    - 出力画像の生成場所
- samples
    - サンプルファイルが格納
        - 01_web_cam_show.py
            - webカメラの画像を表示
            - キーボードから's'入力で画像を保存
                - `./output/01`へ保存
            - キーボードから'q'入力で終了
        - 02_color_convert.py
            - `./data/nabekuro.png`をグレースケール化し二値化
            - グレースケール化画像と二値化画像を保存
                - `./output/02`へ保存
        - 03_back_diff.py
            - `./data/foreground.png`と`./data/background.png`を用いて背景差分を行い保存
                - `./output/03`へ保存
        - 04_mask.py
            - マスク処理のサンプル
                - `./output/04`へ保存
        - 05_dilate_erode.py
            - 膨張処理と縮小処理のサンプル
                - `./output/05`へ保存

## Other

バグや修正案などあればお知らせください

