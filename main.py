from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("MineSweeper")

    button = QPushButton
