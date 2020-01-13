import os
import sys
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QMainWindow, QFileDialog, QProgressBar


class Window(QMainWindow):

    current_dir = ''

    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('ui/interface.ui', self)

        button_images_browse = self.button_images_browse
        button_images_browse.clicked.connect(self.button_images_browse_handler)

        button_pdf_browse = self.button_pdf_browse
        button_pdf_browse.clicked.connect(self.button_pdf_browse_handler)

        button_other_files_browse = self.button_other_files_browse
        button_other_files_browse.clicked.connect(self.button_other_files_browse_handler)

        button_save_settings = self.button_save_settings
        if button_save_settings.isEnabled():
            button_save_settings.clicked.connect(self.button_save_settings_handler)

        self.show()

    def button_images_browse_handler(self):
        dirname = QFileDialog.getExistingDirectory()
        input_pictures = self.input_images
        input_pictures.setText(dirname)

    def button_pdf_browse_handler(self):
        dirname = QFileDialog.getExistingDirectory()
        input_pdf = self.input_pdf
        input_pdf.setText(dirname)

    def button_other_files_browse_handler(self):
        dirname = QFileDialog.getExistingDirectory()
        input_other_files = self.input_other_files
        input_other_files.setText(dirname)

    def button_save_settings_handler(self):
        progressBar = self.progressBar

        button_save_settings = self.button_save_settings

        #print(button_save_settings.isEnabled())

        button_save_settings.setEnabled(False)

        if progressBar.value() == 0 or progressBar.value() == 100:
            i = 0
            while i != 101:
                progressBar.setValue(i)
                time.sleep(0.01)
                i = i + 1

        button_save_settings.setEnabled(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())