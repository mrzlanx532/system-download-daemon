import os


class Common:

    @staticmethod
    def current_directory():
        return os.path.dirname(os.path.dirname(__file__))