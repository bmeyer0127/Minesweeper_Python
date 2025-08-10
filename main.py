import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
  QApplication, 
  QMainWindow,
  QGridLayout,
  QHBoxLayout,
  QVBoxLayout,
  QWidget,
  QPushButton,
  QLCDNumber,
  )
from TileNumber import TileNumber
from CustomButton import CustomButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("MineSweeper")
    # self.setFixedSize(QSize(600,500))

    widget = QWidget()
    gridLayout = QGridLayout()
    horizLayout = QHBoxLayout()
    self.tileButtons = []
    self.tileNumbers = []
    gameBoardWidth = 15
    gameBoardHeight = 10

    for i in range(gameBoardHeight):
      for j in range(gameBoardWidth):
        # tileButton = TileButton(j,i)
        tileButton = CustomButton(j,i)
        tileNumber = TileNumber(j,i)
        self.tileButtons.append(tileButton)
        self.tileNumbers.append(tileNumber)
        gridLayout.addWidget(tileNumber.getTileNumber(), (i), (j))
        gridLayout.addWidget(tileButton.getTileButton(), (i), (j))
    
    gridLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

    widget.setLayout(gridLayout)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()