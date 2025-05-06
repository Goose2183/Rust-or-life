
from content import text
from gui.labels import LabelCreate
from gui.button import CreateBtns
from config import label_rust, label_life, geometry

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title(text.title_name)
        self.root.geometry(geometry)
        self.root.resizable(False, False)

        self.label_manager = LabelCreate(root)
        self.label_manager.create_label(label_rust["text"], label_rust["cords"])
        self.label_manager.create_label(label_life["text"], label_life["cords"])

        self.btn_create = CreateBtns(root)