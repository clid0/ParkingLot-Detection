
import cv2
import pickle
import cvzone
import numpy as np

# Video feed
cap = cv2.VideoCapture('D:\MK\Coding\OJ\parkinglot\gopro.mp4')

with open('D:\MK\Coding\OJ\CarParkPos4', 'rb') as f:
    posList = pickle.load(f)
    print(posList)

width, height = 50, 40


def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        ls = pos
        rect = cv2.boundingRect(ls)
        x, y, w, h = rect
        croped = imgPro[y:y+h, x:x+w].copy()

        ls = ls - ls.min(axis=0)
        mask = np.zeros(croped.shape[:2], np.uint8)
        cv2.drawContours(mask, [ls], -1, (255, 255, 255), -1, cv2.LINE_AA)

        dst = cv2.bitwise_and(croped, croped, mask=mask)

        count = cv2.countNonZero(dst)
        count2 = np.sum(dst == 0)
        count = count2 / (count + count2)

        if count > 0.70:
            color = (0, 255, 0)
            thickness = 2
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.polylines(img, np.int32([pos]), True, color, thickness)
        str_count = "{:.2f}".format(count)
        # cvzone.putTextRect(img, str_count, (x, y + height - 3), scale=1,
        #    thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                       thickness=5, offset=20, colorR=(0, 200, 0))


while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)  # blur의 정도를 결정함
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 3)  # 맨 마지막 값이 선명도를 이야기함.
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=2)

    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    cv2.imshow("ImageMedian", imgMedian)
    cv2.imshow("ImageDilate", imgDilate)
    cv2.waitKey(1)
