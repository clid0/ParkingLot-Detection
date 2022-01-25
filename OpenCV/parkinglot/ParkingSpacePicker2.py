import cv2
import pickle
import numpy as np

print(cv2.__version__)

width, height = 50, 40

try:
    with open('D:\MK\Coding\OJ\CarParkPos2', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
    posList2 = []
    cnt = 0

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
        else:
            posList.append(np.array(posList2))
            cnt = 0
            posList2.clear()
            posList2.append((x, y))
            cnt += 1
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList2):
            x1, y1 = pos
            ls = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList2.pop(i)

    with open('D:\MK\Coding\OJ\CarParkPos2', 'wb') as f:
        pickle.dump(posList, f)


while True:
    img = cv2.imread('D:\MK\Coding\OJ\parkinglot\carParkImg2.png')
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
