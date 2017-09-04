import cv2

img=cv2.imread("galaxy.jpg",0)

print(type(img))
resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg",resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()