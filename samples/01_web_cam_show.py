# import
import os
import cv2

# main
def main():
    # get camera
    cap = cv2.VideoCapture(0)
    
    # save image counter
    save_number = 0

    # loop
    while True:
        # get frame
        ret, frame = cap.read()
        # failed to get image
        if not ret:
            break

        # key input
        key = cv2.waitKey(1)
        # if key input is 'q'
        if key == ord('q'):
            # break this loop
            break
        # if key input is 's'
        elif key == ord('s'):
            # save path 
            save_path = os.path.join(
                '../output/01',
                str(save_number) + '.png')
            # save now frame
            cv2.imwrite(save_path, frame)

            # count up
            save_number += 1

        # showing image
        cv2.imshow("Frame", frame)

    # memory release
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

