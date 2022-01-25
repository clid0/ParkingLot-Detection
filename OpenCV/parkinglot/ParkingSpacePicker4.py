import cv2
import pickle
import numpy as np

print(cv2.__version__)

width, height = 50, 40
cnt = 0
posList2 = []

try:
    with open('D:\MK\Coding\OJ\CarParkPos4', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


# def mouseClick(events, x, y, flags, params):
#     if events == cv2.EVENT_LBUTTONDOWN:
#         posList.append((x, y))
#     if events == cv2.EVENT_RBUTTONDOWN:
#         for i, pos in enumerate(posList):
#             x1, y1 = pos
#             if x1 < x < x1 + width and y1 < y < y1 + height:
#                 posList.pop(i)

#     with open('D:\MK\Coding\OJ\CarParkPos', 'wb') as f:
#         pickle.dump(posList, f)


def mouseClick(events, x, y, flags, params):
    global cnt
    if events == cv2.EVENT_LBUTTONDOWN:
        if cnt < 4:
            posList2.append((x, y))
            cnt += 1
        if cnt == 4:
            posList.append(np.array(posList2))
            cnt = 0
            posList2.clear()
            # posList2.append((x, y))
            # cnt += 1
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, ls in enumerate(posList):
            print(ls)
            x1, y1 = ls[0][0], ls[0][1]
            ls = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('D:\MK\Coding\OJ\CarParkPos4', 'wb') as f:
        pickle.dump(posList, f)


while True:
    img = cv2.imread('D:\MK\Coding\OJ\parkinglot\carParkImg4.png')
    # print(img)
    for pos in posList:
        # cv2.rectangle(img, pos, (pos[0] + width,
        #               pos[1] + height), (255, 0, 255), 2)
        cv2.polylines(img, np.int32([pos]), True, (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)

# img = cv2.imread('D:\MK\Coding\OJ\parkinglot\carParkImg.png')
# cv2.imshow("Image", img)
