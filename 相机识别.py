import cv2  
  
# 创建一个VideoCapture对象，参数0通常表示默认摄像头  
cap = cv2.VideoCapture(0)  
  
# 检查摄像头是否成功打开  
if not cap.isOpened():  
    print("Error: Could not open camera.")  
    exit()  
  
while True:  
    # 从摄像头捕获一帧  
    ret, frame = cap.read()  
      
    # 如果正确读取帧，ret为True  
    if not ret:  
        print("Failed to grab frame")  
        break  
      
    # 调整图片大小  
    frame_resized = cv2.resize(frame, (1024, 800))  
      
    # 转换为灰度图  
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)  
      
    # 显示灰度图  
    cv2.imshow('Gray Camera Feed', gray)  
      
    # 按下'q'键退出循环  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
# 释放VideoCapture对象  
cap.release()  
# 销毁所有OpenCV创建的窗口  
cv2.destroyAllWindows()