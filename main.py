from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QMainWindow
from PyQt5 import uic
import tkfilebrowser
import sys, os
class Window(QMainWindow):

    current_dir = ''

    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('ui/interface.ui', self)

        btn_browse_pictures = self.button_images_browse
        btn_browse_pictures.clicked.connect(self.button_images_browse_)

        self.show()

    def button_images_browse_(self):
        input_pictures = self.input_images
        input_pictures.setText('lorem ipsum')
        #tkfilebrowser.askopendirname()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())