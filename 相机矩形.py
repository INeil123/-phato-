import cv2  
from PIL import Image, ImageDraw, ImageFont 
import numpy as np
  
# 创建一个VideoCapture对象，参数0通常表示默认摄像头  
cap = cv2.VideoCapture(0)  
width = 640
height = 480
  
# 检查摄像头是否成功打开  
if not cap.isOpened():  
    print("Error: Could not open camera.")  
    exit()  
  
# 定义矩形的顶点坐标（这里以左上角和右下角为例）  
# 注意：这些坐标是相对于调整大小后的图像的  
top_left_corner = (100, 100)  # 矩形的左上角坐标  
bottom_right_corner = (400, 300)  # 矩形的右下角坐标  
  
# 定义矩形的颜色（BGR格式）和线型  
rectangle_color = (0, 255, 0)  # 绿色  
rectangle_thickness = 2  # 线型粗细  
# 加载支持中文的字体（确保字体文件路径正确）  
font_path = 'C:\\Windows\\Fonts\\arial.ttf'  # 替换为实际字体文件路径  
font_size = 24  
font = ImageFont.truetype(font_path, font_size)  
  
# 要显示的中文文本  
text = "请将电路板放置图形中"  
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
text_color = (255, 255, 255)  # 白色文字  
# 获取文字的尺寸，以便将其居中显示
(text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, font_thickness)
text_x = (width - text_width) // 2
text_y = (height + text_height) // 2

# 在图像上添加文字
cv2.putText(cap, text, (text_x, text_y), font, font_scale, text_color, font_thickness)
while True:  
    # 从摄像头捕获一帧  
    ret, frame = cap.read()  
      
    # 如果正确读取帧，ret为True  
    if not ret:  
        print("Failed to grab frame")  
        break  
      
    # 调整图片大小（如果需要）  
    frame_resized = cv2.resize(frame, (640, 480))  # 这里我改变了大小作为示例  
      
    # 在调整大小后的图像上绘制矩形  
    cv2.rectangle(frame_resized, top_left_corner, bottom_right_corner, rectangle_color, rectangle_thickness)  
      
    # 显示图像  
    cv2.imshow('your our', frame_resized)  
      
    # 按下'q'键退出循环  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
# 释放VideoCapture对象  
cap.release()  
# 销毁所有OpenCV创建的窗口  
cv2.destroyAllWindows()