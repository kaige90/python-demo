import cv2 as cv


# 图片相关操作
def main():
    # 读取图片信息
    img = cv.imread('D:\data\images\\bus_icon_videoRing.png')
    print('图片的大小为为：', img.shape)
    cv.imshow('原图', img)  # 建立名为‘image’ 的窗口并显示图像
    k = cv.waitKey(0)  # waitkey代表读取键盘的输入，括号里的数字代表等待多长时间，单位ms。 0代表一直等待
    if k == 27:  # 键盘上Esc键的键值
        cv.destroyAllWindows()
    # 缩放图片
    x, y = img.shape[0:2]
    # 缩小图片
    size = (int(y * 0.5), int(x * 0.5))
    shrink = cv.resize(img, size, interpolation=cv.INTER_AREA)
    cv.imshow("缩小", shrink)
    cv.waitKey()
    # 放大图片
    fx = 2
    fy = 2
    enlarge = cv.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv.INTER_CUBIC)
    cv.imshow("放大", enlarge)
    cv.waitKey()


main()
