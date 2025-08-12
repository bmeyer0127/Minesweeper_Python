import sys
from PyQt6.QtCore import Qt, QSize
from pathlib import Path
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
    bombCoordinates = []

    self.setWindowTitle("MineSweeper")
    # self.setFixedSize(QSize(600,500))

    widget = QWidget()
    gridLayout = QGridLayout()
    horizLayout = QHBoxLayout()
    self.tileButtons = []
    self.tileNumbers = []
    self.numberCoordinates = []
    self.bombCoordinates = []
    numberOfBombs = 20
    gameBoardWidth = 10
    gameBoardHeight = 10
    self.possibleCoordinates = []

    # Create possible coordinates for bombs to take sample of
    for i in range(gameBoardHeight):
      for j in range(gameBoardWidth):
        self.possibleCoordinates.append([j,i])

    # Create bomb coordinates
    self.bombCoordinates = random.sample(self.possibleCoordinates, numberOfBombs)
    
    # Create Bombs
    for i in range(len(self.bombCoordinates)):
      tileNumber = TileNumber(self.bombCoordinates[i][0],self.bombCoordinates[i][1],0,True)
      self.tileNumbers.append(tileNumber)
      gridLayout.addWidget(tileNumber.getTileNumber(), (tileNumber.y_pos), (tileNumber.x_pos))

    # Create number tiles and buttons
    for i in range(gameBoardHeight):
      for j in range(gameBoardWidth):
        adjacentBombs = 0
        if ([j,i] not in self.bombCoordinates):
          for bomb in self.bombCoordinates:
            if (i-1 == bomb[1] or i+1 == bomb[1] or i == bomb[1]) and (j-1 == bomb[0] or j+1 == bomb[0] or j == bomb[0]): 
              adjacentBombs += 1
          # tileButton = CustomButton(j,i)
          tileNumber = TileNumber(j,i,adjacentBombs)
          # self.tileButtons.append(tileButton)
          self.tileNumbers.append(tileNumber)
          gridLayout.addWidget(tileNumber.getTileNumber(), (i), (j))
          # gridLayout.addWidget(tileButton.getTileButton(), (i), (j))
        tileButton = CustomButton(j,i,self.bombCoordinates)
        self.tileButtons.append(tileButton)
        gridLayout.addWidget(tileButton.getTileButton(), (i), (j))

    
    gridLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

    widget.setLayout(gridLayout)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)
app.setStyleSheet(Path('assets/styles/Styles.qss').read_text())

window = MainWindow()
window.show()

app.exec()