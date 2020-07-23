import cv2
import numpy as np
import argparse as arg

def process(input_path, output_dir, step, type_name):
    stream = analyze(input_path, step)
    convert(stream, output_dir, type_name)

def analyze(input_path, step):
    stream = []

    cap = cv2.VideoCapture(input_path)

    if cap.isOpened() == False:
        print("error")
        
    i = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if i%step == 0 :
            if ret:
                #print("{} {}".format(i, i%step))
                stream.append(frame)
            else :
                print("vid_end")
                break
        i+=1
    cap.release()
    return stream

def convert(stream, output_dir, type_name):
    digit = len(str(len(stream)))
    for i in range(len(stream)):
        name = '0' * (digit - len(str(i))) + str(i)
        cv2.imwrite("{}/{}.{}".format(output_dir, name, type_name), stream[i])

def main():
    parser = arg.ArgumentParser()
    parser.add_argument('input', type=str, help="Where is video?")
    parser.add_argument('output_dir', type=str, help="Where is target to save image?")
    parser.add_argument('step', type=int, help="What is the value of step?")
    parser.add_argument('type', type=str, help="What is the type of image?")

    args = parser.parse_args()
    process(args.input, args.output_dir, args.step, args.type)

    
if __name__=="__main__":
    main()
