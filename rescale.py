import cv2 as cv


img = cv.imread('resources/photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def chageRes(width, height):
    pass


rescaled_img = rescaleFrame(img)
cv.imshow('Rescaled image', rescaled_img)

# capture = cv.VideoCapture('resources/videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()

#     rescaled_frame = rescaleFrame(frame)

#     cv.imshow('Video', frame)
#     cv.imshow('Rescaled Video', rescaled_frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


cv.waitKey(0)