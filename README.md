## 環境構築
1. 事前に[Anaconda](https://www.anaconda.com/products/distribution)をインストールしておく
2. `env.yaml`を使って環境をインストールする
```
conda env create -f env.yaml
```
3. 構築した仮想環境の確認
```
conda info -e
```

<br />

## 仮想環境の有効化
```
conda activate tkinter
```
<br />

## ライブラリのインストール
<br>

```
pip install googletrans==4.0.0-rc1
```

## EXEファイルの起動
<br>

translatorフォルダの`translator.exe`を起動する。