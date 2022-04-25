# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:41:00 2022

@author: CW
"""

# -*- coding:utf-8 -*-
import cv2
import numpy as np

def drawCircle_kps(src, keypoints):
    dst = src.copy()
    H = src.shape[0] # x low lim
    W = src.shape[1] # y right lim
    offsetScale = 1.1
    
    for i in range(1, len(keypoints)):
        y0 = keypoints[i].pt[0] # max --> W
        x0 = keypoints[i].pt[1] # max --> H
        r = keypoints[i].size
        grayVaule = 0
        
        theta_arr = np.array([0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]) * np.pi
        for theta in theta_arr :
            x_circle = np.int32(x0 + r * np.sin(theta) * offsetScale)
            y_circle = np.int32(y0 + r * np.cos(theta) * offsetScale)
            # boundary check
            if x_circle < 0 :
                x_circle = 0
            if x_circle > (H-1) :
                x_circle = (H-1)
            if y_circle < 0 :
                y_circle = 0
            if y_circle > (W-1) :
                y_circle = (W-1)
            grayVaule += dst[x_circle, y_circle]
        grayVaule /= theta_arr.size

        dst_grayVaule = grayVaule
        dst = cv2.circle(dst, \
            (np.int32(keypoints[i].pt[0]), np.int32(keypoints[i].pt[1])), \
            radius = np.int32(keypoints[i].size*1.05), \
            color = dst_grayVaule, thickness = -1)
            
    return dst

filename = "init"
# Read image
im = cv2.imread(filename+".png", cv2.IMREAD_GRAYSCALE)

# 设置SimpleBlobDetector_Params参数
params = cv2.SimpleBlobDetector_Params()
# 改变阈值
params.minThreshold = 10
params.maxThreshold = 1500

FLAG_switch = True
# 按颜色
params.filterByColor = FLAG_switch
params.blobColor = 255
# 通过面积大小滤波
params.filterByArea = FLAG_switch
params.minArea = 10
params.maxArea = 400
# 通过圆度滤波
params.filterByCircularity = FLAG_switch
params.minCircularity = 0.6
params.maxCircularity = 1
# 通过凸度滤波
params.filterByConvexity = FLAG_switch
params.minConvexity = 0.7
params.maxConvexity = 1
# 通过惯性比滤波
params.filterByInertia = False
params.minInertiaRatio = 0.1
params.maxInertiaRatio = 1
# 创建一个检测器并使用默认参数
detector = cv2.SimpleBlobDetector_create(params)
# 检测blobs
key_points = detector.detect(im)
print(len(key_points))

# 绘制blob的红点
# draw_image = cv2.drawKeypoints(im, key_points, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
draw_image = drawCircle_kps(im, key_points)
 
# Show blobs
# cv2.imshow("key_points", draw_image)
# cv2.waitKey(0)
cv2.imwrite(filename+"_post.png", draw_image)
