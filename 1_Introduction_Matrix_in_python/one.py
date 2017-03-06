
# 0. Input the needed libraries
from scipy import misc
import numpy as np
from scipy import ndimage

# 0. Read the image as gray scale
image  = misc.imread('lena.jpg',mode="L")

# 1. print out the type of the image
print type(image)
print '-' * 50

# 2. Declare a 2D matrix 
mat = np.array([  [1,2,3],[4,5,6],[7,8,9] ])

# 3. print out the type of the matrix
print type(image)
print '-' * 50

# 4. Print the content of image
print image
print image.shape
print '-' * 50

# 5. print the content of matrix 
print mat
print mat.shape




# ----END OF THE CODE-----