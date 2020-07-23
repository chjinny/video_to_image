import cv2
import numpy as np
import argparse as arg

class Converter:
    def __init__(self):
        super().__init__()
        self.total = 100
        self.fin = 0
        self.is_seted = False
        self.is_analyzed = False

    def setup(self, input_path, output_dir, step, type_name):
        self.input_path = input_path
        self.output_dir = output_dir
        self.step = step
        self.type_name = type_name
        self.stream = []
        self.is_seted = True

    def analyze(self):
        cap = cv2.VideoCapture(self.input_path)

        if cap.isOpened() == False:
            print("error")
            
        i = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if i%self.step == 0 :
                if ret:
                    #print("{} {}".format(i, i%step))
                    self.stream.append(frame)
                else :
                    break
            i+=1
        cap.release()
        self.total = len(self.stream)
        self.is_analyzed = True

    def convert(self):
        length = len(self.stream)
        digit = len(str(length))
        for i in range(length):
            name = '0' * (digit - len(str(i))) + str(i)
            cv2.imwrite("{}/{}.{}".format(self.output_dir, name, self.type_name), self.stream[i])
            self.fin = i

def main():
    parser = arg.ArgumentParser()
    parser.add_argument('input', type=str, help="Where is video?")
    parser.add_argument('output_dir', type=str, help="Where is target to save image?")
    parser.add_argument('step', type=int, help="What is the value of step?")
    parser.add_argument('type', type=str, help="What is the type of image?")

    args = parser.parse_args()
    converter = Converter()
    converter.setup(args.input, args.output_dir, args.step, args.type)
    converter.analyze()
    converter.convert()

    
if __name__=="__main__":
    main()
