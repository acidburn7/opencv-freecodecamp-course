import cv2 as cv
import numpy as np


img = cv.imread('resources/photos/park.jpg')
cv.imshow('Cat', img)
# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

# Edge cascade
edge = cv.Canny(blur, 125, 175)
# cv.imshow('Edge', edge)

# Dilating image
dilated = cv.dilate(edge, (37, 7), iterations=3)

# Eroding
erode = cv.erode(dilated, (3, 3), iterations=3)

# Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)

# Crapping
cropped = img[50:200, 200:400]

cv.imshow('Resize', cropped)
cv.waitKey(0)
