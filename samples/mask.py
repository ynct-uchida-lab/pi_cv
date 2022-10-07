# import
import cv2

# main
def main():
    # sample image read 
    img = cv2.imread('../data/nabekuro.png')

    # RGB to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # make mask image
    threshold, img_mask = cv2.threshold(
        img_gray, 0, 255, cv2.THRESH_OTSU)
    
    img_masked = cv2.bitwise_and(img, img, mask=img_mask)
    
    # save
    cv2.imwrite('../output/04/masked.png', img_masked)

if __name__ == '__main__':
    main()

