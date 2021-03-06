import sys
import os
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit, QSystemTrayIcon, QStyle, QAction, QMenu
from PyQt5.QtGui import QIcon
from helpers.alert import Alert
from helpers.validator import Validator
from helpers.tray import Tray
from helpers.common import Common
import json


class Window(QMainWindow):

    def __init__(self):

        super(Window, self).__init__()
        uic.loadUi('ui/main.ui', self)

        self.SC_alert = Alert(self.MainWidget)
        self.SC_tray_icon = Tray(self)

        self.setWindowIcon(QIcon(os.path.join(Common.current_directory(), 'icon.png')))

        button_images_browse = self.button_images_browse
        button_images_browse.clicked.connect(self.button_images_browse_handler)

        button_downloads_browse = self.button_downloads_browse
        button_downloads_browse.clicked.connect(self.button_downloads_browse_handler)

        button_pdf_browse = self.button_pdf_browse
        button_pdf_browse.clicked.connect(self.button_pdf_browse_handler)

        button_other_files_browse = self.button_other_files_browse
        button_other_files_browse.clicked.connect(self.button_other_files_browse_handler)

        button_save_settings = self.button_save_settings
        button_save_settings.clicked.connect(self.button_save_settings_handler)

        button_start_daemon = self.button_start_daemon
        button_start_daemon.clicked.connect(self.button_start_daemon_handler)

        try:
            file = open(os.path.join(Common.current_directory(), 'paths.json'), 'r')
            content = json.loads(file.read())
            if content:
                self.input_downloads.setText(content.get('downloads'))
                self.input_pdf.setText(content.get('pdf_files'))
                self.input_images.setText(content.get('images_files'))
                self.input_other_files.setText(content.get('other_files'))
        except FileNotFoundError:
            pass

        self.show()

    def button_downloads_browse_handler(self):
        dirname = QFileDialog.getExistingDirectory()
        input_downloads = self.input_downloads
        input_downloads.setText(dirname)

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

        button_save_settings = self.button_save_settings

        paths = {
            "downloads": self.input_downloads.text(),
            "pdf_files": self.input_pdf.text(),
            "images_files": self.input_images.text(),
            "other_files": self.input_other_files.text()
        }

        paths = json.dumps(paths)

        file = open(os.path.join(Common.current_directory(), 'paths.json'), 'w+')
        file.write(paths)
        file.close()

        self.SC_alert.show_info("Уведомление", "Путь сохранен!")

    def button_start_daemon_handler(self):

        if not Validator.check_path_from_text([self.input_images, self.input_pdf, self.input_other_files]):
            self.SC_alert.show_warning('Поля не заполнены', 'Пожалуйста, заполните корректно поля')
        else:
            self.SC_tray_icon.show()
            self.hide()
            self.SC_alert.show_info("Уведомление", "Приложение продолжает работать в свернутом режиме")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
