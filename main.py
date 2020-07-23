import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import convert

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video to Images')
        self.setWindowIcon(QIcon('./icon.png'))
        #self.move(500, 500)
        self.resize(400, 200)
        #self.setGeometry(300, 300, 300, 200)
        
        self.forms = ["Video Input", "Folder Output"]
        self.pushButtons = []
        self.labels = []
        self.buttonFuncs = [self.file_input, self.folder_output] 
        self.layout = QVBoxLayout()

        for i in range(len(self.forms)):    
            self.pushButtons.append(QPushButton(self.forms[i]))
            self.pushButtons[i].clicked.connect(self.buttonFuncs[i])
            self.labels.append(QLabel())
            self.layout.addWidget(self.pushButtons[i])
            self.layout.addWidget(self.labels[i])

        label = QLabel()
        label.setText("Image Type")
        self.layout.addWidget(label)
        
        self.rbtn1 = QRadioButton('JPG', self)
        self.rbtn1.setChecked(True)
        self.layout.addWidget(rbtn1)

        self.rbtn2 = QRadioButton('PNG', self)
        self.layout.addWidget(rbtn2)

        self.pushButtons.append(QPushButton("Convert"))
        self.pushButtons[-1].clicked.connect(self.convert)
        self.layout.addWidget(self.pushButtons[-1])
        self.setLayout(self.layout)

    def file_input(self):
        fname = QFileDialog.getOpenFileName(self)
        self.labels[0].setText(fname[0])
    
    def folder_output(self):
        fname = QFileDialog.getExistingDirectory(self)
        self.labels[1].setText(fname)

    def pushButtonClicked(self):
        items = ("KOSPI", "KOSDAK", "KONEX")
        item, ok = QInputDialog.getItem(self, "시장선택", "시장을 선택하세요.", items, 0, False)
        if ok and item:
            self.label.setText(item)

    def convert(self):
        input_file = self.labels[0]
        output_dir = self.labels[1]
        convert_type = ""
        if self.rbtn1.isChecked():
            convert_type = "png"
        else: # self.rbtn1.isChecked():
            convert_type = "jpg"

        convert.convert(input_file, output_dir, step, type_name)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   ex.show()
   app.exec_()