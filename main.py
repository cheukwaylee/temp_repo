# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:41:00 2022

@author: CW
"""

# -*- coding:utf-8 -*-
from turtle import color
import cv2
import numpy as np

def drawCircle_kps(src, keypoints):
    dst = src.copy()
    for i in range(1, len(keypoints)):

        aroundColor = src[np.int32(keypoints[i].pt[0]), np.int32(keypoints[i].pt[1])]

        print(aroundColor)
        dst = cv2.circle(src, \
            (np.int32(keypoints[i].pt[0]), np.int32(keypoints[i].pt[1])), \
            radius = np.int32(keypoints[i].size), \
            color = (0, 0, 255), thickness = -1)
    return dst

filename = "/home/cw/code/IR_image_preProcess_py/1"
# Read image
im = cv2.imread(filename+".png", cv2.IMREAD_GRAYSCALE)

# 设置SimpleBlobDetector_Params参数
params = cv2.SimpleBlobDetector_Params()
# 改变阈值
params.minThreshold = 0
params.maxThreshold = 1500

# 按颜色
params.filterByColor = False
params.blobColor = 255
# 通过面积大小滤波
params.filterByArea = False
params.minArea = 10
params.maxArea = 150
# 通过圆度滤波
params.filterByCircularity = False
params.minCircularity = 0.8
params.maxCircularity = 1
# 通过凸度滤波
params.filterByConvexity = False
params.minConvexity = 0.91
params.maxConvexity = 1
# 通过惯性比滤波
params.filterByInertia = False
params.minInertiaRatio = 0.2
params.maxInertiaRatio = 1
# 创建一个检测器并使用默认参数
detector = cv2.SimpleBlobDetector_create(params)
# 检测blobs
key_points = detector.detect(im)
print(len(key_points))

# 绘制blob的红点
# draw_image = cv2.drawKeypoints(im, key_points, np.array([]), (0, 255, 255), \
#     cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
draw_image = drawCircle_kps(im, key_points)
 
# Show blobs
# cv2.imshow("key_points", draw_image)
# cv2.waitKey(0)
cv2.imwrite(filename+"_post.png", draw_image)
