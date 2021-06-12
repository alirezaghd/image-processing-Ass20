import cv2


image = cv2.imread('3.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

rows = image.shape[0]
cols = image.shape[1]
print(rows, cols)


M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst = cv2.warpAffine(image,M,(cols,rows))

image_s = cv2.resize(dst,(960,528))

cv2.imshow('show output',image_s)
cv2.waitKey()