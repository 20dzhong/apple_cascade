import cv2
import numpy as np
import os

# data dir holds cascade file
# info dir holds
def pics():
    num = 51
    cap = cv2.VideoCapture(1)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        resize = cv2.resize(frame, (100, 100))
        cv2.imshow("pics", resize)
        # waitKey returns 32 bits, 0xFF will convert to 8 bit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('a'):
            path = './sample'
            cv2.imwrite(os.path.join(path, '{}.jpg'.format(num)), frame)
            print("pic" + str(num))
            num += 1

    cap.release()
    cv2.destroyAllWindows()


def create_pos_n_neg():
    for file_type in ['negative']:
        for img in os.listdir(file_type):

            if file_type == 'sample':
                line = file_type + '/' + img + ' 1 0 0 100 100\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'negative':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)


def to_gray():
    pic_num = 51
    for i in range(9):
        img = cv2.imread("./sample/{}.jpg".format(pic_num))
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("./sample/{}.jpg".format(pic_num), gray_image)
        pic_num += 1


to_gray()