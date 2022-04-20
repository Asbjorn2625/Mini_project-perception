import numpy as np
import cv2 as cv
import os
import math

class FruitClass:
    def __init__(self):
        self.aspect = []
        self.meanint = []
        self.extent = []
        self.redmean = []
        self.greenmean = []
        self.bluemean = []
        self.circularity = []

    def lists(self, Fruit, low, high,showimage):
        for i in range(low, high):
            picfruit = "%s/%s_%s.jpg" % (Fruit, Fruit, str(i))
            if os.path.exists(picfruit):
                fruit = cv.imread(picfruit)
                scale_percent = 20  # percent of original size
                width = int(fruit.shape[1] * scale_percent / 100)
                height = int(fruit.shape[0] * scale_percent / 100)
                dim = (width, height)
                # resize image
                resized = cv.resize(fruit, dim, interpolation=cv.INTER_AREA)
                blurApple = cv.medianBlur(resized, 7)
                HSVImg = cv.cvtColor(blurApple, cv.COLOR_BGR2HSV)
                HHigh1 = 255;
                HLow1 = 0
                SHigh1 = 255;
                SLow1 = 103
                Vhigh1 = 255;
                Vlow1 = 0
                redmask1 = cv.inRange(HSVImg, (HLow1, SLow1, Vlow1), (HHigh1, SHigh1, Vhigh1))
                HHigh = 255;
                HLow = 0
                SHigh = 255;
                SLow = 54
                Vhigh = 255;
                Vlow = 0
                redmask2 = cv.inRange(HSVImg, (HLow, SLow, Vlow), (HHigh, SHigh, Vhigh))
                if np.mean(redmask2) < 30:
                    Redmask = redmask2
                else:
                    Redmask = redmask1
                kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (27, 27))
                closing = cv.morphologyEx(Redmask, cv.MORPH_CLOSE, kernel)
                contours, hierarchy = cv.findContours(closing, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
                im_grey = cv.cvtColor(closing, cv.COLOR_GRAY2BGR)
                moodle = cv.bitwise_and(resized, im_grey)
                for k in range(len(contours)):
                    cnt = contours[k]
                    area = cv.contourArea(cnt)
                    x, y, w, h = cv.boundingRect(cnt)
                    perimeter = cv.arcLength(cnt, True)
                    if area > 20000:
                        crop = moodle[y:y + h, x:x + w]
                        circularity = (4 * np.pi * area / (perimeter ** 2))
                        self.circularity.append(circularity)
                        self.aspect.append(float(w) / h)
                        self.meanint.append(np.mean(crop))
                        self.extent.append(float(area) / (w * h))
                        self.redmean.append(cv.mean(crop)[2])
                        self.greenmean.append(cv.mean(crop)[1])
                        self.bluemean.append(cv.mean(crop)[0])
                    if showimage == "show":
                        cv.imshow("Mask", closing)
                        cv.imshow("Original image", fruit)
                        cv.waitKey(1)


def knn2(k, TrainarrX, TrainarrY, TrainarrZ, newarrX, newarrY, newarrZ, fruitinterval):
    distancefruit0 = []
    distancefruit1 = []
    distancefruit2 = []
    fruit0count = 0
    fruit1count = 0
    fruit2count = 0
    normx = max(TrainarrX)
    normy = max((TrainarrY))
    normz = max(TrainarrZ)
    for i in range(len(TrainarrX)):
        dis = math.sqrt(math.pow((TrainarrX[i]/normx)-(newarrX/normx), 2) + math.pow(
            (TrainarrY[i]/normy)-(newarrY/normy), 2) + math.pow((TrainarrZ[i]/normz)-(newarrZ/normz), 2))
        if i <= fruitinterval[0]:
            distancefruit0.append(dis)
        elif fruitinterval[0] < i <= fruitinterval[1]:
            distancefruit1.append(dis)
        elif fruitinterval[1] < i <= fruitinterval[2]:
            distancefruit2.append(dis)
    distancefruit0.sort()
    distancefruit1.sort()
    distancefruit2.sort()
    del distancefruit0[k + 1:len(distancefruit0)]
    del distancefruit1[k + 1:len(distancefruit1)]
    del distancefruit2[k + 1:len(distancefruit2)]
    fulldistancefruit = distancefruit0 + distancefruit1 + distancefruit2
    fulldistancefruit.sort()
    for j in range(k):
        if distancefruit0.count(fulldistancefruit[j]) >= 1:
            fruit0count = fruit0count + 1
        if distancefruit1.count(fulldistancefruit[j]) >= 1:
            fruit1count = fruit1count + 1
        if distancefruit2.count(fulldistancefruit[j]) >= 1:
            fruit2count = fruit2count + 1
    wow = [fruit0count, fruit1count, fruit2count]
    maxi = max(wow)
    nearn = wow.index(maxi)
    if nearn == 0:
        nearfruit = "Apple"
    if nearn == 1:
        nearfruit = "Pear"
    if nearn == 2:
        nearfruit = "Orange"
    return nearfruit


def testing(k, trainX, trainY, trainz, newX, newY, newZ, size, fruit, fruitInterval):
    applecount = 0
    pearcount = 0
    orangeCount = 0
    for x in range(size):
        count = knn2(k, trainX, trainY, trainz, newX[x], newY[x], newZ[x], fruitInterval)
        if count == "Apple":
            applecount = applecount + 1
        elif count == "Pear":
            pearcount = pearcount + 1
        elif count == "Orange":
            orangeCount = orangeCount + 1
    print("percentage of %s %.1f" % (fruit[0], applecount * 100 / (x + 1)))
    print("percentage of %s %.1f" % (fruit[1], pearcount * 100 / (x + 1)))
    print("percentage of %s %.1f" % (fruit[2], orangeCount * 100 / (x + 1)))
