# 0. Input the needed libraries
from scipy import misc
import numpy as np
from scipy import ndimage
from scipy import signal
import cv2

# 0. Read the image as gray scale
image  = misc.imread('lena.jpg',mode="L")

# 1. Make our own matrix to perform convolution
mat = np.array([[103,105,108],[255,102,101],[103,107,255]])
print mat
print '-' * 50

# 2. Define our kernel 
kernel = np.ones((3,3),np.float64)/9
print kernel
print '-' * 50

# 3. Perform the convolution operation 
mat_2 = signal.convolve2d(mat, kernel, boundary='fill', mode='same',fillvalue = 0)

# 4. print the out put 
print mat_2
print '-' * 50

# 5. Print the values of the image again
print image
print '-' * 50

# 6. kernal operation on the image 
image_ker = signal.convolve2d(image, kernel, boundary='fill', mode='same',fillvalue = 0)
print image_ker
print '-' * 50





