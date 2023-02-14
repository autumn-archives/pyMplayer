# pyMplayer beta

pyMplayerは、pySimpleGUIとpygameを使用して作られたシンプルなオーディオプレーヤーです。
OGG形式のオーディオファイルに対応しています。

![sample1](https://user-images.githubusercontent.com/124559210/218642280-ac79be90-91a2-48c1-99bc-aba27c4e1051.png)

# Features

pyMplayerはたくさんのテーマから好きなものを選んで使用できます。
change_theneボタンから、テーマの一覧を表示して、好きなテーマに切り替えられます。
![choose_theme](https://user-images.githubusercontent.com/124559210/218649753-a695a039-cd41-439b-963a-461d21f60f84.png)

![pull_down](https://user-images.githubusercontent.com/124559210/218650000-a7aadfcc-dd91-43e4-a5a8-80776570d4e0.png)

切り替えたテーマは、change_themeの右にある保存ボタンで保存可能です。
次回以降から選択したテーマでpyMplayerを起動できます。

![choose_theme_after](https://user-images.githubusercontent.com/124559210/218650202-e19eecf4-3230-4f73-9c72-56b0e4936ae8.png)

![bandicam 2023-02-14 14-18-08-111](https://user-images.githubusercontent.com/124559210/218650334-b34ae5b3-ba66-4560-9a20-c7cd0ad18cb0.png)

これは、テーマの一例です。他にもたくさんのテーマがあります。
![theme_list](https://user-images.githubusercontent.com/124559210/218655925-d8f3fc24-3fe0-4cd4-b268-1884255e5618.jpg)
# Requirement


* Python                    3.10.5
* PySimpleGUI               4.60.1
* pygame                    2.1.2
* librosa                   0.9.2
* configparser              5.3.0


# Installation


```bash
pip install PySimpleGUI
pip install pygame
pip install librosa
pip install configparser
```

# Usage

main.pyをPythonで実行してください。

```bash
python main.py
```

"pyMplayer" is Confidential.