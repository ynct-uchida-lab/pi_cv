# import
import cv2

# main
def main():
    # sample image read 
    img = cv2.imread('../data/nabekuro.png')

    # RGB to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # save grayscale image
    cv2.imwrite('../output/02/gray.png', img_gray)

    # Binarization
    # Automatically determine the threshold
    threshold, img_bin = cv2.threshold(
        img_gray, 0, 255, cv2.THRESH_OTSU)
    # save bin. image
    cv2.imwrite('../output/02/bin.png', img_bin)

if __name__ == '__main__':
    main()

