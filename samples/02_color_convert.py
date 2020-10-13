# import
import cv2

# main
def main():
    img = cv2.imread('../data/cat.png')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('../output/gray.png', img_gray)

if __name__ == '__main__':
    main()

