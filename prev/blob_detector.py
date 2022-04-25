# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:41:00 2022

@author: CW
"""

# -*- coding:utf-8 -*-
import cv2
import numpy as np

filename = "C:\\Users\\CW\\Desktop\\thesis_ws\\Snipaste_2022-04-22_12-06-05"
# Read image
im = cv2.imread(filename+".png", cv2.IMREAD_GRAYSCALE)
 
# 设置SimpleBlobDetector_Params参数
params = cv2.SimpleBlobDetector_Params()
# 改变阈值
params.minThreshold = 0
params.maxThreshold = 1500

# 按颜色
params.filterByColor = True
params.blobColor = 255
# 通过面积大小滤波
params.filterByArea = True
params.minArea = 10
params.maxArea = 150
# 通过圆度滤波
params.filterByCircularity = True
params.minCircularity = 0.8
params.maxCircularity = 1
# 通过凸度滤波
params.filterByConvexity = True
params.minConvexity = 0.91
params.maxConvexity = 1
# 通过惯性比滤波
params.filterByInertia = True
params.minInertiaRatio = 0.2
params.maxInertiaRatio = 1
# 创建一个检测器并使用默认参数
detector = cv2.SimpleBlobDetector_create(params)
# 检测blobs.
key_points = detector.detect(im)
 
# 绘制blob的红点
draw_image = cv2.drawKeypoints(im, key_points, np.array([]), (0, 0, 255),
                               cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show blobs
# cv2.imshow("key_points", draw_image)
# cv2.waitKey(0)
cv2.imwrite(filename+"_post.png", draw_image)

