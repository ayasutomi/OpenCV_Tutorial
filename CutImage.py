import cv2

img = cv2.imread('imgs/watch.jpg', cv2.IMREAD_COLOR)
#resize
img2 = cv2.resize(img,None,fx=0.35, fy=0.35, interpolation = cv2.INTER_AREA)

img2 = img2[70:120, 90:140]


cv2.imwrite("imgs/watchSmall.jpg",img2) #save image

cv2.imshow('image', img)
cv2.imshow('image2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
