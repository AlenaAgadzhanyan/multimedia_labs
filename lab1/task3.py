import cv2

cap = cv2.VideoCapture("C:/Users/Honor/Pictures/Camera Roll/WIN_20250906_10_11_13_Pro.mp4", cv2.CAP_ANY)

while True:
    ret, frame = cap.read()
    if not(ret):
        break
    frame = cv2.resize(frame, (500, 500))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27: 
        break