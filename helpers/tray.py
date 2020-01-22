import os
from PyQt5.QtWidgets import QSystemTrayIcon, QAction, QMenu, QWidget
from PyQt5.QtGui import QIcon
from helpers.common import Common

class Tray:

    def __init__(self, target_platform: QWidget):

        self.target_platform = target_platform
        self.tray_icon = QSystemTrayIcon()

        show_action = QAction("Show", self.target_platform)
        quit_action = QAction("Exit", self.target_platform)
        hide_action = QAction("Hide", self.target_platform)

        show_action.triggered.connect(self.target_platform_show)
        hide_action.triggered.connect(self.target_platform.hide)
        quit_action.triggered.connect(self.target_platform.close)

        tray_menu = QMenu()

        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.setIcon(QIcon(os.path.join(Common.current_directory(), 'tray.png')))

    def target_platform_show(self):
        print(self)
        print(self.target_platform)


    def show(self):
        self.tray_icon.show()

    def hide(self):
        self.tray_icon.hide()

    def close(self):
        self.tray_icon.close()