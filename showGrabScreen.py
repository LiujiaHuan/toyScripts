#————————————————————#
#email:cheayuki13@gmail.com
#usr:LiuJiahuan
#time:2022-2-5
#————————————————————#

from grabscreen import grab_screen
import cv2
x, y = (3840, 2160) #分辨率
re_x, re_y = (3840, 2160)   #显示范围，用于窗口大小操作
while True:
    img =  grab_screen(region=(0, 0, 3840, 2160))  #调用屏幕截取

    cv2.namedWindow('windowname', cv2.WINDOW_NORMAL)    #创建新窗口
    cv2.resizeWindow('windowname', re_x // 3, re_y // 3)    #指定窗口大小
    cv2.imshow('windowname', img)           #展示frame
    #设置窗口始终在最上面
    hwnd = win32gui.FindWindow(None,'windowname')   #获取句柄
    CVRECT = cv2.getWindowImageRect('windowname')   #返回窗口的一些参数
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE) #设置到顶层，不改变大小，可自由移动


    if cv2.waitKey(1) & 0xFF == ord('q'):   #程序结束逻辑
        cv2.destroyAllWindows()
        break


