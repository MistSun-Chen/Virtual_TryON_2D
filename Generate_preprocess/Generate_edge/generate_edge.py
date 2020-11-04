import cv2


'''
#读取灰度图片
image = cv2.imread("test.jpg")
# image = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("gray.jpg",image)
#binary(黑白二值）,ret代表阈值，80是低阈值，255是高阈值
ret,image1 = cv2.threshold(image,80,255,cv2.THRESH_BINARY)

cv2.imwrite("binary.jpg",image1)

#二值图像的反色处理，将图片像素取反
height,width,channel = image1.shape #返回图片大小

image2 = image1.copy()

for i in range(height):
    for j in range(width):
        image2[i,j] = (255-image1[i,j])

#image2为反色处理后的图片
cv2.imwrite("invert.jpg",image2)


#边缘提取，使用Canny函数
image2_3 = cv2.Canny(image2,80,255)#设置80为低阈值，255为高阈值
cv2.imwrite("edge.jpg",image2_3)

#再次对图像进行反色处理使提取的边缘为黑色，其余为白色，方法同image2
height1,width1 = image2_3.shape
image3 =image2_3.copy()

for i in range(height1):
    for j in range(width1):
        image3[i,j] = (255-image2_3[i,j])

cv2.imwrite("invert_s.jpg",image3)

'''


#############################
#***************************#
#############################
#another method pic filter

src = cv2.imread("test.jpg")
#均值滤波
des = cv2.blur(src,(5,5))
cv2.imwrite("des.jpg",des)
#中值滤波
med = cv2.medianBlur(src,5)
cv2.imwrite("med.jpg",med)

#高斯滤波
gauss =cv2.GaussianBlur(src,(5,5),0)
cv2.imwrite("gauss.jpg",gauss)

#高斯边缘检测
gaussedge = cv2.Canny(gauss,0,50)
cv2.imwrite("gaussedge.jpg",gaussedge)



