#change content at a specific pixel
import cv2
import numpy
img=cv2.imread("pikachu1.jpg",1)
# import pdb; pdb.set_trace()
# img.item(100,100,2)
for i in range(200):
    img.itemset((100,i,0),200)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# b,g,r = cv2.split(img)
# img[:,:,2] = 0

# dst = cv2.addWeighted(img1,0.7,img2,0.3,0) read two img and then



# # Load two images
# img1 = cv2.imread('messi5.jpg')
# img2 = cv2.imread('opencv_logo.png')

# # I want to put logo on top-left corner, So I create a ROI
# rows,cols,channels = img2.shape
# roi = img1[0:rows, 0:cols ]

# # Now create a mask of logo and create its inverse mask also
# img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)

# # Now black-out the area of logo in ROI
# img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# # Take only region of logo from logo image.
# img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# # Put logo in ROI and modify the main image
# dst = cv2.add(img1_bg,img2_fg)
# img1[0:rows, 0:cols ] = dst

# cv2.imshow('res',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()