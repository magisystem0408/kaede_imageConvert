# 楓のやつ
## 仕様
2つのgeoTiff画像を決めた法則に従って重ね合わせて新しい画像を生成する。

![aza](https://user-images.githubusercontent.com/61937077/159150569-b3eb4218-b1de-48b3-90ca-53a414bef6d1.png)

### 楓が要求する重ね合わせの時のアルゴリズム
![IMG_1835](https://user-images.githubusercontent.com/61937077/159150685-695e5100-466f-4e9e-b2b4-e8f1567847e4.jpg)

### 実行結果(main.py)
![Figure_1](https://user-images.githubusercontent.com/61937077/160282485-6ae5eb4f-ba18-4105-acb3-fbeda5092d10.png)

#### kmeansによる色使用率分析(colorDevider.py)
![colorDevider](https://user-images.githubusercontent.com/61937077/160282584-e8d31fb1-53e9-4543-92dd-f0f25aa8969f.png)

## Install Modules
```
pip install -r requirements.txt
```

## Start main
```
python main.py
```

