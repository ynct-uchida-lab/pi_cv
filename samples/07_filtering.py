import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    # image read
    img = cv2.imread('../data/Lenna.bmp')
    # RGB to GrayScale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # average filter
    img_blur = cv2.blur(img,(5, 5))

    # sobel filter
    img_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
    img_sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)

    # laplacian filter
    img_laplacian = cv2.Laplacian(img_gray, cv2.CV_64F)

    # save bin. image
    cv2.imwrite('../output/07/average.png', img_blur)
    cv2.imwrite('../output/07/sobel_x.png', img_sobel_x)
    cv2.imwrite('../output/07/sobel_y.png', img_sobel_y)
    cv2.imwrite('../output/07/laplacian.png', img_laplacian)

if __name__ == '__main__':
    main()

