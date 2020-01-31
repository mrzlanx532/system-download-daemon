import os
from PyQt5.QtWidgets import QSystemTrayIcon, QMainWindow, QAction, QMenu, QWidget
from PyQt5.QtGui import QIcon
from helpers.common import Common


class Tray:

    def __init__(self, target_platform: QMainWindow):

        self.target_platform = target_platform
        self.tray_icon = QSystemTrayIcon()

        show_action = QAction("Show", self.target_platform)
        quit_action = QAction("Exit", self.target_platform)

        show_action.triggered.connect(self.target_platform_show)
        quit_action.triggered.connect(self.target_platform_close)

        tray_menu = QMenu()

        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.setIcon(QIcon(os.path.join(Common.current_directory(), 'tray.png')))

    def target_platform_show(self):
        self.target_platform.show()
        self.tray_icon.hide()

    def target_platform_close(self):
        self.target_platform.close()

    def show(self):
        self.tray_icon.show()

    def hide(self):
        self.tray_icon.hide()
        self.target_platform.show()
