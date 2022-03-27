import rasterio as rs
from matplotlib import pyplot as plt

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
                    generateCol.append(100)
                else:
                    generateCol.append(200)
            else:
                # それ以外はoldValueの値をgenerateColのlistに追加
                # generateCol.append(oldArray[row][col])
                if oldArray[row][col] == 0:
                    generateCol.append(10)
                else:
                    generateCol.append(50)

        # generateColをgenerateImgの配列に入れて行列化
        generateImg.append(generateCol)
    # pltに読み込ませて表示する
    plt.imshow(generateImg)
    plt.imsave('generate.png', generateImg)
    plt.plot(10,10,label="Land",color="#440154")
    plt.plot(10, 10, label="SeaLand", color="#22898d")
    plt.plot(10, 10, label="LandSea", color="#fde724")
    plt.plot(10, 10, label="Sea", color="#3f4587")
    plt.legend(loc=(0.1, 0.1))
    plt.show()

