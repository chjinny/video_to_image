import cv2
import numpy as np
import argparse as arg
import os

class Converter:
    def __init__(self):
        super().__init__()
        self.total = 100
        self.step = 1
        self.fin = 0
        self.is_seted = False
        self.is_analyzed = False
        self.stream = []

    def setup(self, input_path, output_dir, step, type_name):
        self.input_path = os.path.normcase(input_path)
        self.output_dir = os.path.normcase(output_dir)
        self.step = step
        self.type_name = type_name

    def analyze(self):
        cap = cv2.VideoCapture(self.input_path)
        self.total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        if cap.isOpened() == False:
            print("error")
            
        i = 0
        j = 0
        digit =len(str(self.total)) 
        while(cap.isOpened()):
            ret, frame = cap.read()
            if i%self.step == 0 :
                if ret:
                    #print("{} {}".format(i, i%step))
                    #self.stream.append(frame)
                    name = '0' * (digit - len(str(j))) + str(j)
                    cv2.imwrite("{}/{}.{}".format(self.output_dir, name, self.type_name), frame)
                    j += 1
                else :
                    break
            i+=1
        cap.release()
        self.is_analyzed = True

    def process(self, input_path, output_dir, step, type_name):
        print(input_path, output_dir, step, type_name)
        print("start setup")
        self.setup(input_path, output_dir, step, type_name)
        print("start analyze")
        self.analyze()

def main():
    parser = arg.ArgumentParser()
    parser.add_argument('input', type=str, help="Where is video?")
    parser.add_argument('output_dir', type=str, help="Where is target to save image?")
    parser.add_argument('step', type=int, help="What is the value of step?")
    parser.add_argument('type', type=str, help="What is the type of image?")

    args = parser.parse_args()
    converter = Converter()
    converter.process(args.input, args.output_dir, args.step, args.type)


    
if __name__=="__main__":
    main()
