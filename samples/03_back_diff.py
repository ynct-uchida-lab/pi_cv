# import
import cv2

# main
def main():
    # sample image read 
    img_fore = cv2.imread('../data/foreground.png')
    # sample background image read 
    img_back = cv2.imread('../data/background.png')

    # RGB to grayscale
    img_fore_gray = cv2.cvtColor(img_fore, cv2.COLOR_BGR2GRAY)
    img_back_gray = cv2.cvtColor(img_back, cv2.COLOR_BGR2GRAY)

    # background difference
    img_diff = cv2.absdiff(img_fore_gray, img_back_gray)
    
    # save
    cv2.imwrite('../output/03/sub.png', img_sub)

if __name__ == '__main__':
    main()

