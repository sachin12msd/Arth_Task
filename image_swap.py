import cv2
import matplotlib.pyplot as plt


img1= cv2.imread('im1.jpg')
img2 = cv2.imread('im2.jpg')
img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img1)


img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
plt.imshow(img2)


img3= img1[0:100, 75:145]
img4= img2[15:145, 40:140]


img4= cv2.resize(img4,(70,100))
img3= cv2.resize(img3,(100,130))


img4.shape


img1[0:100, 75:145] = img4
img2[15:145, 40:140] = img3

img3.shape

img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
cv2.imshow('Swapped image',img1)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('Swapped Image',img2)
cv2.waitKey()
cv2.destroyAllWindows()
