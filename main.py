import cv2
import numpy as np
import argparse as arg

def main():
    parser = arg.ArgumentParser()
    parser.add_argument('video', type=str, help="Where is video?")
    parser.add_argument('image', type=str, help="Where is target to save image?")
    parser.add_argument('step', type=int, help="What is the value of step?")
    parser.add_argument('type', type=str, help="What is the type of image?")

    args = parser.parse_args()
    video = args.video
    image = args.image
    step = args.step
    type_name = args.type

    cap = cv2.VideoCapture(video)

    i = 0
    if cap.isOpened() == False:
        print("error")
    while(cap.isOpened()):
        if i%step == 0 :
            ret, frame = cap.read()
            if ret:
                cv2.imwrite("{}/{}.{}".format(image, i//step, type_name), frame)
            else :
                print("error")
        i+=1
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
