import rasterio as rs
from matplotlib import pyplot

img1989 = r'imgs/0318LandSea1989.tif'
img2021 = r'imgs/0318LAndSea2021.tif'


def makePixelData(oldImg, NewImg):
    oldArray = rs.open(oldImg).read(1)
    newArray = rs.open(NewImg).read(1)
    return oldArray, newArray

if __name__ == '__main__':
    oldArray, newArray = makePixelData(img1989, img2021)

    generateImg = []
    for row in range(len(oldArray)):
        generateRow = []
        for col in range(len(oldArray[row])):
            oldValue = oldArray[row][col]
            if not oldValue == newArray[row][col]:
                if oldValue == 1:
                    generateRow.append(0)
                else:
                    generateRow.append(1)
            else:
                generateRow.append(oldArray[row][col])
        generateImg.append(generateRow)
    pyplot.imshow(generateImg)
    pyplot.show()
