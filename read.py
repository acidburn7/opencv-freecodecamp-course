import cv2 as cv


img = cv.imread('resources/photos/cat_large2.jpg')
cv.imshow('Cat', img)

# Reading videos
# capture = cv.VideoCapture('resources/videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()

#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

cv.waitKey(0)