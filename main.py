import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import converter as cvt
import threading

class ThreadClass_converter(QThread): 
    def __init__(self, parent = None): 
        super(ThreadClass_converter,self).__init__(parent)
    def set_arg(self, obj, arg):
        self.arg = arg
        self.obj = obj
    def run(self): 
        self.obj.process(self.arg[0], self.arg[1], self.arg[2], self.arg[3])
    
    def __del__(self): 
        self.wait()


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.threadclass_converter = ThreadClass_converter() 
        self.converter = cvt.Converter()
        self.convert_on = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video to Images')
        self.setWindowIcon(QIcon('./icon.png'))
        self.resize(400, 200)

        self.pushButtons = []
        self.labels = []
        self.layout = QVBoxLayout()

        # path selection  
        # 00 input path 
        self.pushButtons.append(QPushButton("Video Input"))
        self.pushButtons[-1].clicked.connect(self.file_input)
        self.labels.append(QLabel())
        self.layout.addWidget(self.pushButtons[-1])
        self.layout.addWidget(self.labels[-1])

        # 11 output path
        self.pushButtons.append(QPushButton("Folder Output"))
        self.pushButtons[-1].clicked.connect(self.folder_output)
        self.labels.append(QLabel())
        self.layout.addWidget(self.pushButtons[-1])
        self.layout.addWidget(self.labels[-1])
        
        # 21 type select
        self.labels.append(QLabel())
        self.labels[-1].setText("Image Type")
        self.layout.addWidget(self.labels[-1])
        
        # 22 JPG 
        self.pushButtons.append(QRadioButton('JPG', self))
        self.pushButtons[-1].setChecked(True)
        self.layout.addWidget(self.pushButtons[-1])

        # 23 PNG
        self.pushButtons.append(QRadioButton('PNG', self))
        self.layout.addWidget(self.pushButtons[-1])

        # 33 step
        self.labels.append(QLabel())
        self.labels[-1].setText("Step : {}".format(self.converter.step))
        self.layout.addWidget(self.labels[-1])
        self.step_bar = QSlider(Qt.Horizontal, self)
        self.step_bar.valueChanged.connect(self.step_val)
        self.layout.addWidget(self.step_bar)

       
        # 34 Convert
        self.pushButtons.append(QPushButton("Convert"))
        self.pushButtons[-1].clicked.connect(self.convert)
        self.pushButtons[-1].clicked.connect(self.toggle)
        self.layout.addWidget(self.pushButtons[-1])


        # 44 process bar
        '''
        self.pbar = QProgressBar(self)

        self.layout.addWidget(self.pbar)
        '''
        self.setLayout(self.layout)

    def step_val(self):
        self.converter.step = self.step_bar.value()
        self.labels[3].setText("Step : {}".format(self.converter.step))
        self.step_bar.setMaximum(100)
        self.step_bar.setMinimum(1)
        self.step_bar.setPageStep(10)
        self.step_bar.setSingleStep(1)

    def timer(self) :
        rate = self.converter.fin/self.converter.total
        self.pbar.setValue(self.converter.fin/self.converter.total)
        #self.pbar.setValue(50)
        if rate >= 100:
            self.t.cancel()

    def file_input(self):
        fname = QFileDialog.getOpenFileName(self)
        self.labels[0].setText(fname[0])
        self.input_path = fname[0]

    def folder_output(self):
        fname = QFileDialog.getExistingDirectory(self)
        self.labels[1].setText(fname)
        self.output_dir = fname

    def toggle(self):
        if self.convert_on == False:
            self.pushButtons[4].setText("Stop")
            self.convert_on = True
        else: #state == "Stop":
            self.pushButtons[4].setText("Convert")
            self.threadclass_converter.terminate()
            self.convert_on = False

    def convert(self):
        self.type_name = ""
        if self.pushButtons[3].isChecked():
            self.type_name = "png"
        else: # self.rbtn1.isChecked():
            self.type_name = "jpg"

        if self.converter.total < self.converter.step:
            print("error")
        arg = [self.input_path, self.output_dir, self.converter.step, self.type_name]
        #self.t = threading.Timer(1, self.timer())
        #self.t.start()
        self.threadclass_converter.set_arg(self.converter, arg) 
        self.threadclass_converter.start() 

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   ex.show()
   app.exec_()