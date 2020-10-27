# import
import cv2
import numpy as np

# main
def main():

    # Elements for dilation / erosion
    kernel_4 = np.array([[0,1,0],[1,1,1],[0,1,0]], np.uint8)
    kernel_8 = np.array([[1,1,1],[1,1,1],[1,1,1]], np.uint8)

    # Sample image read (gray scale)
    img_gray = cv2.imread(
        '../data/dilate_erode.png',
        cv2.IMREAD_GRAYSCALE)

    # Binarization
    # Automatically determine the threshold
    threshold, img_bin = cv2.threshold(
        img_gray, 0, 255, cv2.THRESH_OTSU)

    # Dilation
    img_dilate = cv2.dilate(img_bin, kernel_8, iterations=1)
    # Erosion
    img_erode = cv2.erode(img_bin, kernel_8, iterations=1)

    # Display
    cv2.imshow('Original', img_bin)
    cv2.imshow('Dilate', img_dilate)
    cv2.imshow('Erode', img_erode)
    # Close display by key input
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # save
    cv2.imwrite('../output/05/dilate.png', img_dilate)
    cv2.imwrite('../output/05/erode.png', img_erode)

if __name__ == '__main__':
    main()

