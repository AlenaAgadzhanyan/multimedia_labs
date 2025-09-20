import cv2

folder = "D:/NFT-marketplace/img"

img1 = cv2.imread(r'D:/NFT-marketplace/img/collection.png', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread(r'D:/NFT-marketplace/img/creatorbackground-4.jpg', cv2.IMREAD_ANYDEPTH)
img3 = cv2.imread(r"C:/Users/Honor/Downloads/amal.webp", cv2.INTER_LINEAR)

cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
cv2.namedWindow('Display window', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Display window', cv2.WINDOW_FULLSCREEN)

cv2.imshow('Display window', img1)
cv2.imshow('Display window', img2)
cv2.imshow('Display window', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()