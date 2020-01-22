import os

class Validator:

    @staticmethod
    def check_path_from_text(objects = []):
        for obj in objects:
            if not os.path.isdir(obj.text()):
                return False
        return True


