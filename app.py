#from textblob import TextBlob


#print(TextBlob("Mein kampf").translate(to="en"))

import cv2


import pytesseract

import os

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


options = "-l swe"

imageDir = './test_img'

listOfImgs = os.listdir(imageDir)

for filename in listOfImgs:
    if '.jpeg' in filename.lower():
        print(filename)
        image = cv2.imread(imageDir+'/'+filename)
        dimensions = image.shape
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        rev = pytesseract.image_to_string(rgb, config=options)
        print(rev)
