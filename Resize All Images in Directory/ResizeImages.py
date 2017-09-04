import os
import cv2

for file in os.listdir("./"):
    if file.endswith(".jpg"):
        print(file)
        img = cv2.imread(file, 0)
        resized_img = cv2.resize(img, (100,100))
        cv2.imwrite(file +"_resized.jpg", resized_img)