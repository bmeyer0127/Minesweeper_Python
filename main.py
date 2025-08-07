import sys

from MinesweeperButton import TileButton

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
  QApplication, 
  QMainWindow, 
  QGridLayout,
  QWidget,
  QPushButton,
  QSpinBox,
  QLabel,
  QLCDNumber,
  QProgressBar,
  )

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("MineSweeper")
    self.setFixedSize(QSize(600,500))

    layout = QGridLayout()

    gameBoardWidth = 5
    gameBoardHeight = 6


    for i in range(gameBoardHeight):
      for j in range(gameBoardWidth):
        layout.addWidget(TileButton(j,i).getTileButton(), i, j)
    
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()