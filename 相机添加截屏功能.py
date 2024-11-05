import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import time

top_left_corner = (100, 100)  # 矩形的左上角坐标
bottom_right_corner = (500, 400)  # 矩形的右下角坐标

# 定义矩形的颜色（BGR格式）和线型
rectangle_color = (0, 255, 0)  # 绿色
rectangle_thickness = 2  # 线型粗细

# 假设这里已经有了add_chinese_text函数的正确定义
def add_chinese_text(image, text, position, font_path, font_size, color):
    img_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, fill=color, font=font)
    return cv2.cvtColor(np.asarray(img_pil), cv2.COLOR_RGB2BGR)


# 初始化视频捕获对象（这里假设摄像头索引为0，可根据实际情况调整）
cap = cv2.VideoCapture(0)

# 设置截屏保存的文件夹路径
save_folder = "screenshots"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

while True:
    # 读取视频帧
    ret, frame = cap.read()

    if not ret:
        break

    # 在OpenCV图像上绘制矩形框（先绘制矩形框，后续再添加文字）
    cv2.rectangle(frame, top_left_corner, bottom_right_corner, rectangle_color, rectangle_thickness)

    # 在帧上添加中文文字，调整文字位置使其在矩形框内看起来比较合适
    text_position = (top_left_corner[0] + 10, top_left_corner[1] + 10)  # 示例位置，可根据需求调整
    frame_with_text = add_chinese_text(frame, "将电路板放置框内", text_position, "simsun.ttc", 30, (255, 255, 255))

    # 显示带有文字和矩形框的视频帧
    cv2.imshow("相机画面", frame_with_text)

    # 等待按键事件，这里等待1毫秒
    key = cv2.waitKey(1)

    # 如果按下's'键，进行截屏操作
    if key == ord('s'):
        # 生成截屏文件名，这里使用当前时间作为文件名的一部分，以保证文件名的唯一性
        screenshot_name = f"{save_folder}/screenshot_{int(time.time())}.png"
        cv2.imwrite(screenshot_name, frame_with_text)
        print(f"截屏已保存至 {screenshot_name}")

    # 如果按下'q' 键，退出循环
    elif key == ord('q'):
        break

# 释放视频捕获对象并关闭窗口
cap.release()
cv2.destroyAllWindows()