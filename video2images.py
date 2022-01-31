#——————————————————————————————————#
e-mail: cheayuki13@gmail.com
name: LiuJiahuan
time: 2022-1-30
#__________________________________#
import cv2


def save_image(addr,image,index):
    address = addr + 'img_' + str(index) + '.jpg'
    print(address)
    cv2.imwrite(address,image)


video_path = r'C:\Users\13956\Desktop\yolov5-master\data\labelimg\video'
out_path = 'C:/Users/13956/Desktop/yolov5-master/data/labelimg/images/'

is_all_frame = True   #是否取整个视频，如果否则为选定某一段
start_frame = 1       #如果is_all_frame false, 进入以下两个参数，起始帧，结束帧
end_frame = 1000
time_interval = 8     #多少帧存一次图片
videoCapture = cv2.VideoCapture(video_path)
success, frame = videoCapture.read()

#
i = 0   #遍历所有帧的变量
j = 0   #成功存储图片的索引
while success:
    i += 1
    if i % time_interval == 0:
        if not is_all_frame: #选取部分视频
            if start_frame <= i <= end_frame:
                j += 1
                print("________________Save frame________________", j)
                save_image(out_path, frame, j)
            elif i > end_frame:
                break
        else:     #选取整个视频
            j += 1
            print("__________Save Frame______________")
            save_image(out_path, frame, j)
    success, frame = videoCapture.read()
    
