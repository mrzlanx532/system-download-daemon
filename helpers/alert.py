from PyQt5.QtWidgets import QErrorMessage, QMessageBox, QWidget

class Alert:

    def __init__(self, target_platform: QWidget):
        self.target_platform = target_platform

    def show_error(msg):
        err_obj = QErrorMessage()
        err_obj.showMessage(msg)
        return err_obj.exec_()

    def show_critical(self, msg_1, msg_2):
        wrn_obj = QMessageBox()
        wrn_obj.critical(self.target_platform, msg_1, msg_2)
        wrn_obj.show()

    def show_warning(self, msg_1, msg_2):
        wrn_obj = QMessageBox()
        wrn_obj.warning(self.target_platform, msg_1, msg_2)
        wrn_obj.show()

    def show_info(self, msg_1, msg_2):
        wrn_obj = QMessageBox()
        wrn_obj.information(self.target_platform, msg_1, msg_2)
        wrn_obj.show()

