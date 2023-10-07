import os
class App:
    def __init__(self,root):
        root.geometry("600x400")
        root.title("Đăng ký học phần")
        path = os.path.dirname(__file__)
        image = os.path.join(path, 'image')
        root.iconbitmap(os.path.join(image, 'icon.ico'))
        root["bg"] = "light green"
        root.resizable(False, False)
