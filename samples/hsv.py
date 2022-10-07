# import
import numpy as np
import cv2

# main
def main():
    # sample image read 
    img = cv2.imread('../data/rgb.png')

    # define hsv threshold
    hsv_lower = np.array([0, 155, 155])
    hsv_upper = np.array([10, 255, 255])

    # convert RGB to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # extracted image by hsv threshold
    result_img = cv2.inRange(hsv, hsv_lower, hsv_upper)
    # masking
    output_img = cv2.bitwise_and(img, img, mask=result_img)

    # save
    cv2.imwrite('../output/06/result.png', result_img)
    cv2.imwrite('../output/06/output.png', output_img)

if __name__ == '__main__':
    main()

