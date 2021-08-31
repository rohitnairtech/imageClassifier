import os


from easyocr import Reader

import cv2

import matplotlib.pyplot as plt

reader = Reader(['sv'], gpu = True)

imageDir = './test_img'

listOfImgs = os.listdir(imageDir)

filterList = ['P', 'UDS']


boundedRatio = []

for filename in listOfImgs:
    if '.jpeg' in filename.lower():
        print(filename)
        fullfilename = "".join([imageDir, '/', filename])
        image = cv2.imread(fullfilename, cv2.IMREAD_GRAYSCALE)
        results = reader.readtext(image)
        for (bbox, word, accuracy) in results:
            if accuracy > 0.45 and word not in filterList:
                print(word)
                boundedRatio = bbox

print(boundedRatio)
(tl, tr, br, bl) = boundedRatio

tl = (int(tl[0]), int(tl[1]))
tr = (int(tr[0]), int(tr[1]))
br = (int(br[0]), int(br[1]))
bl = (int(bl[0]), int(bl[1]))

croppedImg = cv2.rectangle(image, tl, br, (0, 255, 0), 2)

plt.imshow(croppedImg)