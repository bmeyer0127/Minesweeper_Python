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
import random
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
    self.numberCoordinates = []
    self.bombCoordinates = []
    numberOfBombs = 5
    gameBoardWidth = 8
    gameBoardHeight = 8

    # Create bomb coordinates
    for i in range(numberOfBombs):
      xCoordinate = random.randint(0,gameBoardWidth-1)
      yCoordinate = random.randint(0,gameBoardHeight-1)
      self.bombCoordinates.append([xCoordinate, yCoordinate])
    
    # Create Bombs
    for i in range(len(self.bombCoordinates)):
      tileNumber = TileNumber(self.bombCoordinates[i][0],self.bombCoordinates[i][1],0,True)
      self.tileNumbers.append(tileNumber)
      gridLayout.addWidget(tileNumber.getTileNumber(), (tileNumber.y_pos), (tileNumber.x_pos))

    # Create number tiles and buttons
    for i in range(gameBoardHeight):
      for j in range(gameBoardWidth):
        adjacentBombs = 0
        for bomb in self.bombCoordinates:
          if (i-1 == bomb[1] or i+1 == bomb[1] or i == bomb[1]) and (j-1 == bomb[0] or j+1 == bomb[0] or j == bomb[0]): 
            adjacentBombs += 1
        tileButton = CustomButton(j,i)
        tileNumber = TileNumber(j,i,adjacentBombs)
        self.tileButtons.append(tileButton)
        self.tileNumbers.append(tileNumber)
        gridLayout.addWidget(tileNumber.getTileNumber(), (i), (j))
        gridLayout.addWidget(tileButton.getTileButton(), (i), (j))
    
    gridLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

    widget.setLayout(gridLayout)
    self.setCentralWidget(widget)
    for bomb in self.bombCoordinates:
      print(bomb)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()