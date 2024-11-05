import cv2
import numpy as np

# 读取给定的图片
given_image = cv2.imread("screenshots\\screenshot_1730712221.png")
# 将给定图片转换为灰度图
given_image_gray = cv2.cvtColor(given_image, cv2.COLOR_BGR2GRAY)


# 初始化ORB特征提取器
orb = cv2.ORB_create()

# 从给定图片中提取特征点和描述子
kp_given, des_given = orb.extractAndDescribe(given_image_gray)

# 初始化视频捕获对象（这里假设摄像头索引为0，可根据实际情况调整）
cap = cv2.VideoCapture(0)

while True:
    # 读取视频帧
    ret, frame = cap.read()

    if not ret:
        break

    # 将视频帧转换为灰度图
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 从视频帧中提取特征点和描述子
    kp_frame, des_frame = orb.extractAndDescribe(frame_gray)

    # 初始化暴力匹配器
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # 对给定图片和视频帧的描述子进行匹配
    matches = bf.match(des_given, des_frame)

    # 根据匹配度对匹配对进行排序
    matches = sorted(matches, key=lambda x: x.distance)

    # 设定一个阈值，用于判断是否认为两张图片相似
    threshold = 0.3

    # 计算匹配对的数量与总特征点数量的比例作为相似度
    total_kp_given = len(kp_given)
    total_kp_frame = len(kp_frame)
    matched_kp_count = len(matches)

    similarity = matched_kp_count / max(total_kp_given, total_kp_frame)

    if similarity >= threshold:
        print("相机画面与给定图片相似")
    else:
            print("相机画面与给定图片不相似")

    # 显示视频帧
    cv2.imshow("相机画面", frame)

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频捕获对象并关闭窗口
cap.release()
cv2.destroyAllWindows()