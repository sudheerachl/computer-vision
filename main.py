# -*- coding: utf-8 -*-


import cv2
import numpy as np
from matplotlib import pyplot as plt

imgbgr=cv2.imread("airplane.png")

plt.imshow(imgbgr)

"""converting bgr to rgb scale

"""

imgrgb=cv2.cvtColor(imgbgr,cv2.COLOR_BGR2RGB)

plt.subplot(1,2,1)
plt.imshow(imgbgr)
plt.title("BGR")
plt.subplot(1,2,2)
plt.imshow(imgrgb)
plt.title("RGB")

rp=imgrgb[:,:,0]
rp

min_rp=np.min(rp)
min_rp

"""converting bgr to gray scale

"""

gray_image = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2GRAY)

plt.imshow(gray_image,cmap='gray')

plt.subplot(1,3,1)
plt.imshow(imgbgr)
plt.title("BGR")
plt.subplot(1,3,2)
plt.imshow(imgrgb)
plt.title("RGB")
plt.subplot(1,3,3)
plt.imshow(gray_image,cmap='gray')
plt.title("GRAY")

rpg=gray_image[:,0]
rpg

min_rpg=np.min(rpg)
min_rpg

"""cropping an image."""

imgcgray=gray_image[127:285,27:493]
plt.imshow(imgcgray,cmap='gray')

plt.subgray_image = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2GRAY)
plt.subplot(1,3,1)
plt.imshow(imgbgr[127:285,27:493])
plt.title("BGRCROP")
plt.subplot(1,3,2)
plt.imshow(imgrgb[127:285,27:493])
plt.title("RGBCROP")
plt.subplot(1,3,3)
plt.imshow(imgcgray,cmap='gray')
plt.title("GRAYCROP")

"""image brightening."""

imgbgrb=imgbgr*2

imgbgrb_30=imgbgr+30
imgbgrb_100=imgbgr+100
plt.subplot(1,3,1)
plt.imshow(imgbgr)
plt.title("BGRCROP")
plt.subplot(1,3,2)
plt.imshow(imgbgrb_30)
plt.title("RGBCROP")
plt.subplot(1,3,3)
plt.imshow(imgbgrb_100)
plt.title("RGBCROP")

imgrgbb_30=imgrgb+30
imgrgbb_100=imgrgb+100
plt.subplot(1,3,1)
plt.imshow(imgrgb)
plt.title("BGRCROP")
plt.subplot(1,3,2)
plt.imshow(imgrgbb_30)
plt.title("RGBCROP")
plt.subplot(1,3,3)
plt.imshow(imgrgbb_100)
plt.title("RGBCROP")

imgrgbbm=imgrgb*2
plt.subplot(1,3,1)
plt.imshow(imgrgb)
plt.title("BGRCROP")
plt.subplot(1,3,2)
plt.imshow(np.uint8(imgrgbbm))

"""bgr to hsv conversion"""

imghsv=cv2.cvtColor(imgbgr, cv2.COLOR_BGR2HSV)
plt.imshow(imghsv)

imghsv=cv2.cvtColor(imgbgrb, cv2.COLOR_BGR2HSV)
plt.imshow(imghsv)

"""RGB to HSV conversion."""

imghsvr=cv2.cvtColor(imgrgb, cv2.COLOR_RGB2HSV)
plt.imshow(imghsvr)

gray_negative = abs(255-gray_image)
plt.imshow(gray_negative,cmap='gray')

"""gray negative conversion.
ImageNegative:
Inverts the intensity values of each pixel(255-original_value).This emphasizes dark areas and hides details inbright areas.
Formula:negative_image=  255 -original_image
"""

plt.subplot(1,3,1)
plt.imshow(gray_image, cmap='gray')
plt.title("gray")
plt.subplot(1,3,2)
plt.imshow(gray_negative,cmap='gray')
plt.title("gray_negative")

"""gamma transform
Formula:gamma_image=original_image**gamma
"""

gamma1=abs(np.power(gray_image,0.3))
gamma2=abs(np.power(gray_image,0.8))
gamma3=abs(np.power(gray_image,1.2))

plt.subplot(1,4,1)
plt.imshow(gray_image, cmap='gray')
plt.title("gray")
plt.subplot(1,4,2)
plt.imshow(np.uint8(gamma1),cmap='gray')
plt.title("gamma1")
plt.subplot(1,4,3)
plt.imshow(np.uint8(gamma2),cmap='gray')
plt.title("gamma2")
plt.subplot(1,4,4)
plt.imshow(np.uint8(gamma3),cmap='gray')
plt.title("gamma3")

"""Log-Transform:
Formula:log_image = c* np.log(1+ original_image)(controls compression)
"""

log_gray1=5*np.log(gray_image+1)
log_gray2=10*np.log(gray_image+1)
log_gray3=15*np.log(gray_image+1)

plt.subplot(1,4,1)
plt.imshow(gray_image, cmap='gray')
plt.title("gray")
plt.subplot(1,4,2)
plt.imshow(np.uint8(log_gray1),cmap='gray')
plt.title("log_gray1")
plt.subplot(1,4,3)
plt.imshow(np.uint8(log_gray2),cmap='gray')
plt.title("log_gray2")
plt.subplot(1,4,4)
plt.imshow(np.uint8(log_gray3),cmap='gray')
plt.title("log_gray3")

rpg=gamma3[:,0]
rpg

"""Image Binarization:
 Converts a grayscale image to a binary image (black and white) by setting pixels below athresholdvalue to 0 andaboveto 255.Formula:binary_image=np.where (original_image<threshold,0,255)
"""

(m,n)=gray_image.shape
img_4=np.zeros([m,n])

gray_image.shape

t=200
for i in range (512):
    for j in range (512):
        if gray_image[i,j]<t:
            img_4[i,j]=0
        else:
            img_4[i,j]=255

plt.imshow(img_4,cmap='gray')

"""Contrast Stretching"""

con=gray_image
xp=[0,35,98,193,255]
fp=[0,23,45,153,255]
x=np.arange(256)
table=np.interp(x,xp,fp).astype('uint8')
con=cv2.LUT(con,table)

plt.subplot(1,3,1)
plt.imshow(gray_image, cmap='gray')
plt.title("gray")
plt.subplot(1,3,2)
plt.imshow(con,cmap='gray')
plt.title("contrast stretching")

plt.subplot(1,2,1)
plt.hist(gray_image.ravel(),256,[0,255],density=1)
plt.title("gray")
plt.subplot(1,2,2)
plt.hist(con.ravel(),256,[0,255],density=1)
plt.title("contrast stretching")

"""IMAGE SMOOTHENING AND IMAGE SHARPENING"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
bgray=cv2.imread("butterfly-gray.jpg")

plt.imshow(bgray)

gray = cv2.cvtColor(bgray, cv2.COLOR_BGR2GRAY)

plt.imshow(gray,cmap="gray")

"""HISTOGRAM EQUALIZATION"""

equal=cv2.equalizeHist(gray)

plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("gray")
plt.subplot(1,2,2)
plt.imshow(equal,cmap='gray')
plt.title("equalized")

plt.subplot(1,2,1)
plt.hist(gray.ravel(),256,[0,255],density=1)
plt.title("gray")
plt.subplot(1,2,2)
plt.hist(equal.ravel(),256,[0,255],density=1)
plt.title("equalized")

"""REMOVING NOISE"""

noise=cv2.imread("noisyimage.jpg",0)
plt.imshow(noise, cmap='gray')

kernel_size=5
kernel=np.ones((kernel_size,kernel_size),np.float32)/100
print(kernel)

smooth=cv2.filter2D(noise,-1,kernel)
smooth

"""IMAGE SMOOTHENING"""

plt.subplot(1,2,1)
plt.imshow(noise, cmap='gray')
plt.title("gray")
plt.subplot(1,2,2)
plt.imshow(smooth,cmap='gray')
plt.title("Smooth")

"""GUASSIAN BLUR"""

blur = cv2.GaussianBlur(noise,(7,),0)

plt.subplot(1,2,1)
plt.imshow(noise, cmap='gray')
plt.title("gray")
plt.subplot(1,2,2)
plt.imshow(blur,cmap='gray')
plt.title("Guassian_blur")

"""IMAGE SHARPENING"""

sharpen_filter=np.array([[0,-1,0],
                 [-1,2,-1],
                [0,-1,0]])
sharp=cv2.filter2D(noise,-1,sharpen_filter)

plt.subplot(1,2,1)
plt.imshow(noise, cmap='gray')
plt.title("gray")
plt.subplot(1,2,2)
plt.imshow(sharp,cmap='gray')
plt.title("Sharp")

b2=cv2.imread("butterfly2.jpeg")
plt.imshow(b2)

"""THRESHOLDING."""

b2gray = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
plt.imshow(b2gray, cmap='gray')

(m,n)=b2gray.shape
img_4=np.zeros([m,n])
b2gray.shape

t=100
t2=150
t3=200
for i in range (176):
    for j in range (286):
        if b2gray[i,j]<t:
            img_4[i,j]=0
        elif((b2gray[i,j]>t) and (b2gray[i,j]<t2)):
            img_4[i,j]=55
        elif((b2gray[i,j]>t2) and (b2gray[i,j]<t3)):
            img_4[i,j]=155
        else:
            img_4[i,j]=255

plt.subplot(1,2,1)
plt.imshow(b2gray, cmap='gray')
plt.title("gray")
plt.subplot(1,2,2)
plt.imshow(img_4,cmap='gray')
plt.title("Threshold")

t=65
t2=100
t3=165
t4=215
t5=250
for i in range (176):
    for j in range (286):
        if b2gray[i,j]<t:
            img_4[i,j]=0
        elif((b2gray[i,j]>t) and (b2gray[i,j]<t2)):
            img_4[i,j]=55
        elif((b2gray[i,j]>t2) and (b2gray[i,j]<t3)):
            img_4[i,j]=155
        elif((b2gray[i,j]>t3) and (b2gray[i,j]<t4)):
            img_4[i,j]=185
        elif((b2gray[i,j]>t4) and (b2gray[i,j]<t5)):
            img_4[i,j]=210
        else:
            img_4[i,j]=255

plt.subplot(1,2,1)
plt.imshow(b2gray, cmap='gray')
plt.title("gray")
plt.subplot(1,2,2)
plt.imshow(img_4,cmap='gray')
plt.title("Threshold")

histg = cv2.calcHist([b2gray],[0],None,[256],[0,256])

plt.plot(histg)
plt.show()

mean1= np.mean(b2gray[0,50])
mean1

mean2= np.mean(b2gray[50,100])
mean2

mean2= np.mean(b2gray[100,176])
mean2



t=50
t2=100
t3=176

for i in range (176):
    for j in range (286):
        if b2gray[i,j]<t:
            img_4[i,j]=141
        elif((b2gray[i,j]>t) and (b2gray[i,j]<t2)):
            img_4[i,j]=173
        elif((b2gray[i,j]>t2) and (b2gray[i,j]<t3)):
            img_4[i,j]=29
        else:
            img_4[i,j]=255

plt.subplot(1,2,1)
plt.imshow(b2gray, cmap='gray')
plt.title("gray")
plt.subplot(1,2,2)
plt.imshow(img_4,cmap='gray')
plt.title("Threshold")



"""EDGE BASED SEGMENTATION."""

b4=cv2.imread("lab4.png")
plt.imshow(b4)

b4gray = cv2.cvtColor(b4, cv2.COLOR_BGR2GRAY)
plt.imshow(b4gray, cmap='gray')

"""VERTICAL"""

#sobelx = np.array([[-1, -1, -1], [2, 2, 2], [-1, -1, -1]])
vert = np.array([[-1, 2, 1], [-1, 2, -1], [-1, 2, -1]])
b4_x = cv2.filter2D(b4gray, -1, sobelvert)

plt.imshow(b4_x, cmap='gray')

"""HORIZONTAL"""

horizontal =  np.array([[-1, -1, -1], [2, 2, 2], [-1, -1, -1]])
b4_h = cv2.filter2D(b4gray, -1, horizontal)

plt.imshow(b4_x, cmap='gray')

"""DIAGONAL"""

diag =  np.array([[-1, -1, 2], [-1, 2, -1], [-1, -1, 2]])
b4_d = cv2.filter2D(b4gray, -1, diag)
plt.imshow(b4_x, cmap='gray')

plt.subplot(1,4,1)
plt.imshow(b4gray,cmap='gray')
plt.title("GRAY")

plt.subplot(1,4,2)
plt.imshow(b4_x,cmap='gray')
plt.title("VERTICAL")
plt.subplot(1,4,3)
plt.imshow(b4_h,cmap='gray')
plt.title("HORIZONTAL")
plt.subplot(1,4,4)
plt.imshow(b4_h,cmap='gray')
plt.title("DIAGONAL")



"""SOBEL KERNAL"""

sobelx=np.array([[-1, -2, -1],[0,0,0],[1,2,1]])
sobely=np.array([[-1, 0, 1],[-2,0,2],[-1,0,1]])
b4_sx = cv2.filter2D(b4gray, -1, sobelx)
b4_sy = cv2.filter2D(b4gray, -1, sobely)
plt.subplot(1,3,1)
plt.imshow(b4gray,cmap='gray')
plt.title("GRAY")
plt.subplot(1,3,2)
plt.imshow(b4_sx ,cmap='gray')
plt.title("SOBELX")
plt.subplot(1,3,3)
plt.imshow(b4_sy,cmap='gray')
plt.title("SOBELY")

plt.imshow(b4_sx ,cmap='gray')

plt.imshow(b4_sy,cmap='gray')

"""PREWITT KERNEL"""

perwitx=np.array([[-1, -1, -1],[0,0,0],[1,1,1]])
perwitty=np.array([[-1, 0, 1],[-1,0,1],[-1,0,1]])
b4_px = cv2.filter2D(b4gray, -1, perwitx)
b4_py = cv2.filter2D(b4gray, -1, perwitty)
plt.subplot(1,3,1)
plt.imshow(b4gray,cmap='gray')
plt.title("GRAY")
plt.subplot(1,3,2)
plt.imshow(b4_px ,cmap='gray')
plt.title("PERWITTX")
plt.subplot(1,3,3)
plt.imshow(b4_py,cmap='gray')
plt.title("PERWITTY")

"""ROBERT KERNEL"""

robertx=np.array([[1, 0],[0,-1]])
roberty=np.array([[ 0, -1],[1,0]])
b4_rx = cv2.filter2D(b4gray, -1, robertx)
b4_ry = cv2.filter2D(b4gray, -1, roberty)
plt.subplot(1,3,1)
plt.imshow(b4gray,cmap='gray')
plt.title("GRAY")
plt.subplot(1,3,2)
plt.imshow(b4_rx ,cmap='gray')
plt.title("ROBERTX")
plt.subplot(1,3,3)
plt.imshow(b4_ry,cmap='gray')
plt.title("ROBERTY")



sobelx=np.array([[-1, -2, -1],[0,0,0],[1,2,1]])
sobely=np.array([[-1, 0, 1],[-2,0,2],[-1,0,1]])
b4_sx = cv2.filter2D(b4gray, -1, sobelx)
b4_sy = cv2.filter2D(b4gray, -1, sobely)
plt.subplot(1,3,1)
plt.imshow(b4gray,cmap='gray')
plt.title("GRAY")
plt.subplot(1,3,2)
plt.imshow(b4_sx ,cmap='gray')
plt.title("SOBELX")
plt.subplot(1,3,3)
plt.imshow(b4_sy,cmap='gray')
plt.title("SOBELY")

b5=cv2.imread("noise.jpg")
plt.imshow(b5)

"""MEDIAN BLUR FOR SALT NOISE IMAGE

"""

median = cv2.medianBlur(b5, 11)
plt.imshow(median)

sobelx=np.array([[-1, -2, -1],[0,0,0],[1,2,1]])
sobely=np.array([[-1, 0, 1],[-2,0,2],[-1,0,1]])
b5_sx = cv2.filter2D(median, -1, sobelx)
b5_sy = cv2.filter2D(median, -1, sobely)
plt.subplot(1,3,1)
plt.imshow(median,cmap='gray')
plt.title("GRAY")
plt.subplot(1,3,2)
plt.imshow(b5_sx ,cmap='gray')
plt.title("SOBELX")
plt.subplot(1,3,3)
plt.imshow(b5_sy,cmap='gray')
plt.title("SOBELY")

plt.imshow(b5_sx ,cmap='gray')

plt.imshow(b5_sy,cmap='gray')





"""GraphCuts:

DividingaNetworkImagine a network of connections, like a social media platform where users are nodes and friendships are edges. Graph cut algorithms come in when you want to split this network into two distinct groups.


•BuildingBlocks:The network itself is a graph, made of vertices (nodes) representing individuals and edges connecting them.

•Vertices:These are the basic units, like users in the social media example, holding information.

•Edges:These connections between users can have weights, indicating the strength of the friendship.

•MakingtheCut:A graph cut divides the vertices into two separate sets (often called S and T).

•EdgesAcrosstheDivide:The cut-set is the collection of edges with one end in S and the other in T.

•MinimizingtheCost:We want a cut that minimizes a cost function. This cost typically comes from adding the weights of all edges in the cut-set.

•FindingtheOptimalSplit:The min-cut problem asks for the cut with the absolute lowest cost function value.


Helping Hands: SeedPoints and  Binary Masks
Sometimes, images can be tricky to segment (separating objects from the background). Graph cuts can benefit from some guidance:

•SeedPoints:Imagine pointing at a specific object in the image and telling the algorithm, "That's definitely the foreground!" These are seed points, which help steer the segmentation process, especially when the image is unclear.

•BinaryMasks:Think of a black and white image where black pixels represent the background and white pixels represent the object. This is a binary mask. It can be created manually or through other techniques, acting as a pre-segmentation that influences the cost function and initial division in graph cut algorithms.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

car=cv2.imread("car.jpg")
plt.imshow(car)



import cv2 as cv
img=car
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (220, 400, 363, 240)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img1 = img*mask2[:,:,np.newaxis]

mask2

plt.imshow(img1)



plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title("img")
plt.subplot(1,2,2)
plt.imshow(img1 ,cmap='gray')
plt.title("Grabcut")

car2=cv2.imread("car2.jpg")
plt.imshow(car2)

import cv2 as cv
img=car2
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (60, 450, 1400, 315)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,1,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img1 = img*mask2[:,:,np.newaxis]

plt.imshow(img1)

plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title("img")
plt.subplot(1,2,2)
plt.imshow(img1 ,cmap='gray')
plt.title("Grabcut")

groot=cv2.imread("groot.jpg")
plt.imshow(groot)

import cv2 as cv
img2=groot
mask = np.zeros(img2.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (840,10, 600, 1400)
cv.grabCut(img2,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img3 = img2*mask2[:,:,np.newaxis]

plt.imshow(img3)

cars=cv2.imread("cars.jpeg")
plt.imshow(cars)

import cv2 as cv
img=cars
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (150, 60, 250,160)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,1,cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img4 = img*mask2[:,:,np.newaxis]

plt.imshow(img4)

import cv2 as cv
img=cars
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (10, 100, 120,60)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,1,cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

mask3 = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect =  (150, 60, 250,160)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,1,cv.GC_INIT_WITH_RECT)

mask4 = np.where((mask3==2)|(mask3==0),0,1).astype('uint8')
img5 =  img*mask4[:,:,np.newaxis]+img*mask2[:,:,np.newaxis]

plt.imshow(img5)

"""ACTIVE CONTOURS

Active Contour Segmentation, also known as the Snake Model, is an image processing technique aiming to locate object boundaries. It employs deformable models, such as the cubic B-spline, renowned for their flexibility and adaptability to diverse shapes.

Initialization: The process starts with an initial contour, often a basic shape like a circle or polygon, placed over the image, initially distant from the object boundary.'

Energy Function: Snake Model utilizes an energy function gauging the discrepancy between the current and ideal contours, closely aligning with the object boundary.

It comprises:

1. Internal Energy (E_int): Encourages smooth contouring, calculated as the sum of squared curvatures, promoting smoother contours.

2. External Energy (E_ext): Draws the contour towards the object boundary by integrating a force function (F(x, y)) along the contour, typically derived from image gradients.Evolution: The contour evolves over time to minimize total energy (E_total = E_int + E_ext), employing calculus of variations and optimization methods like gradient descent.

Stopping Criteria: Evolution halts upon convergence to the object boundary or reaching a predefined iteration limit.

Object Boundary Detection: The final contour depicts the detected object boundary.

Alpha (α): Governs internal forces, influencing contour smoothness and rigidity.

• Low α (< 0.1): Enhances flexibility, risking excessive bending and inaccurate contours, especially with weak edges.

• High α (> 1): Induces stiffness, potentially struggling with highly curved boundaries and getting trapped in local minima.

Beta (β): Regulates external forces influenced by image features.

• Low β (< 10): Reduces sensitivity to features, risking deviation from the actual boundary.

• High β (> 100): Amplifies sensitivity, potentially capturing irrelevant strong edges as part of the boundary.

Gamma (γ): Modulates image intensity's influence on contour movement.

• Low γ (< 0.001): Minimally affected by intensity variations.

 High γ (> 0.1): Heightens sensitivity, beneficial for varied intensity objects, yet excessive values may induce instability.
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour,  morphological_geodesic_active_contour

#load test data
img = data.astronaut()
img = rgb2gray(img)

#Data for creating circular boundary
s = np.linspace(0, 2*np.pi, 400)
r = 100 + 100*np.sin(s)
c = 220 + 100*np.cos(s)
init = np.array([r, c]).T

#Contour (after applying gaussian smoothing)
snake = active_contour(gaussian(img, 3, preserve_range=False),    init, alpha=0.015, beta=10, gamma=0.001)

#CIRCUlAR BOUNDARY
fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(img, cmap=plt.cm.gray)
ax.plot(init[:, 1], init[:, 0],'--r', lw=3)
ax.plot(snake[:, 1], snake[:, 0], '-b', lw=3)
plt.show()



"""Morphological Image Processing:

Morphological image processing encompasses a variety of techniques utilized for analyzing the geometrical structure of an image. These techniques rely on basic set-theoretic operations such as erosion, dilation, opening, closing, and their combinations.

 Typically, these operations are applied to binary images or grayscale images treated as binary sets.
"""

img = cv2.imread('lc.jpg')
img1= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img1,cmap="gray")

ret,thresh = cv2.threshold(img1,70,255,0)
thresh=cv2.bitwise_not(thresh)

"""structuring element-square"""

kernel = np.ones((3, 3), np.uint8)

img_erosion = cv2.erode(thresh, kernel, iterations=1)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)

plt.subplot(1,3,1)
plt.imshow(thresh,cmap="gray")
plt.title("Binary")
plt.subplot(1,3,2)
plt.imshow(img_erosion,cmap="gray")
plt.title("erosion")
plt.subplot(1,3,3)
plt.imshow(img_dilation,cmap="gray" )
plt.title("dilation")

"""structuring element-cross"""

kernel1=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

img_erosion1 = cv2.erode(thresh, kernel1, iterations=1)
img_dilation1 = cv2.dilate(thresh, kernel1, iterations=1)

plt.subplot(1,3,1)
plt.imshow(thresh,cmap="gray")
plt.title("Binary")
plt.subplot(1,3,2)
plt.imshow(img_erosion1,cmap="gray")
plt.title("erosion")
plt.subplot(1,3,3)
plt.imshow(img_dilation1,cmap="gray" )
plt.title("dilation")

kernel2=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

img_erosion2 = cv2.erode(thresh, kernel2, iterations=1)
img_dilation2 = cv2.dilate(thresh, kernel2, iterations=1)

plt.subplot(1,3,1)
plt.imshow(thresh,cmap="gray")
plt.title("Binary")
plt.subplot(1,3,2)
plt.imshow(img_erosion2,cmap="gray")
plt.title("erosion")
plt.subplot(1,3,3)
plt.imshow(img_dilation2,cmap="gray" )
plt.title("dilation")

"""structuring element-diamond."""

diamond=np.array([[0,0,1,0,0,],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]])

img_erosion3 = cv2.erode(thresh, diamond, iterations=1)
img_dilation3 = cv2.dilate(thresh, diamond, iterations=1)

"""watershed algorithm"""

img = cv2.imread('coin.jpeg')
img1= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


plt.imshow(img1,cmap="gray")

ret, thresh = cv2.threshold(img1,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

plt.imshow(thresh,cmap="gray")

#remove noise
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

coin_dilated = cv2.dilate(opening,kernel,iterations=3)
plt.imshow(coin_dilated,cmap="gray")

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

sure_fg = np.uint8(sure_fg)
plt.imshow(sure_fg,cmap="gray")
unknown = cv2.subtract(coin_dilated,sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0



markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

plt.imshow(markers)

plt.subplot(1,3,1)
plt.imshow(thresh,cmap="gray")
plt.title("Binary")
plt.subplot(1,3,2)
plt.imshow(img,cmap="gray")
plt.title("erosion")
plt.subplot(1,3,3)
plt.imshow(markers)
plt.title("dilation")

