import sys

from MinesweeperButton import TileButton

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
  QApplication, 
  QMainWindow,
  QGridLayout,
  QHBoxLayout,
  QVBoxLayout,
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

    widget = QWidget()

    gridLayout = QGridLayout()

    gameBoardWidth = 5
    gameBoardHeight = 6

    self.tileButtons = []

    for i in range(gameBoardHeight):
      for j in range(gameBoardWidth):
        tileButton = TileButton(j,i)
        self.tileButtons.append(tileButton)
        gridLayout.addWidget(tileButton.getTileButton(), (i), (j))
    
    gridLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

    widget.setLayout(gridLayout)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()