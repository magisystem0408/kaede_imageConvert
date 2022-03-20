import rasterio as rs
from matplotlib import pyplot

img1989 = r'imgs/0318LandSea1989.tif'
img2021 = r'imgs/0318LAndSea2021.tif'

# 画像の読み込み。


def makePixelData(oldImg, NewImg):
    # .read(1)は仕様
    oldArray = rs.open(oldImg).read(1)
    newArray = rs.open(NewImg).read(1)
    # それぞれ二次元配列を返す
    return oldArray, newArray


if __name__ == '__main__':
    oldArray, newArray = makePixelData(img1989, img2021)
    # 画像生成処理
    generateImg = []
    for row in range(len(oldArray)):
        # 行を定義
        generateCol = []
        for col in range(len(oldArray[row])):
            # ここで行列の要素を取得できる
            oldValue = oldArray[row][col]
            # oldValueとnewValue(newArray[row][col])の値が違う時に処理する
            if not oldValue == newArray[row][col]:
                if oldValue == 1:
                    generateCol.append(0)
                else:
                    generateCol.append(1)
            else:
                # それ以外はoldValueの値をgenerateColのlistに追加
                generateCol.append(oldArray[row][col])
        # generateColをgenerateImgの配列に入れて行列化
        generateImg.append(generateCol)

    # pltに読み込ませて表示する
    pyplot.imshow(generateImg)
    pyplot.show()
