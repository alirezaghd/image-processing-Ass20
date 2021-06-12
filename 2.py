import cv2

image = cv2.imread('1.jpg')
image2 = cv2.imread('2.jpg')

#image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

rows = image.shape[0]
cols = image.shape[1]


for i in range(rows):
    for j in range(cols):
        image[i, j] = 255 - image[i, j]

rows2 = image2.shape[0]
cols2 = image2.shape[1]

for i in range(rows2):
    for j in range(cols2):
        image2[i, j] = 255 - image2[i, j]


cv2.imshow('show output',image)
cv2.imshow('show output2',image2)
cv2.waitKey()