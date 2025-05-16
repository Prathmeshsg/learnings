# PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(700, 300, 500, 500)
        # self.setWindowIcon(QIcon("profile_pic.jpg"))
        
        # label = QLabel("Hello World!", self)
        # label.setFont(QFont("Arial", 20))
        # label.setGeometry(0, 0, 500, 100)
        # label.move(200, 200)
        # label.setStyleSheet("background-color: red;"
        #                     "color: white;"
        #                     "border-radius: 10px;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;"
        #                     "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignCenter)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) 
        # can use AlignLeft, AlignRight, AlignTop, AlignBottom also
        
        # setting an image on window
        label1 = QLabel(self)
        
        pixmap = QPixmap("./profile_pic.jpg")
        label1.setPixmap(pixmap)
        label1.setScaledContents(True)
        label1.setGeometry((self.width() - label1.width()) // 2,
                           (self.height() - label1.height()) // 2,
                           label1.width(), label1.height())
        
        
        



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()