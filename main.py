import sys
from PyQt6.QtCore import (
  Qt, 
  QSize,
  QTime,
  QTimer
)
from PyQt6.QtWidgets import (
  QApplication, 
  QMainWindow,
  QGridLayout,
  QHBoxLayout,
  QVBoxLayout,
  QStackedLayout,
  QWidget,
  QLabel,
  QPushButton,
  QLCDNumber,
  )
from pathlib import Path
import random
from TileNumber import TileNumber
from CustomButton import CustomButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("MineSweeper")
    self.setFixedSize(QSize(600,500))

    widget = QWidget()
    gridLayout = QGridLayout()
    horizLayout = QHBoxLayout()
    vertLayout = QVBoxLayout()
    self.startButtons = []
    self.time = QTime(0,0,0)
    self.timer = QTimer()
    self.timerWidget = QLCDNumber()
    self.tileButtons = []
    self.tileNumbers = []
    self.numberCoordinates = []
    self.bombCoordinates = []
    numberOfBombs = 20
    self.gameBoardWidth = 10
    self.gameBoardHeight = 10
    self.possibleCoordinates = []

    # Number of bombs display widget
    numberOfBombsDisplay = QLabel()
    numberOfBombsDisplay.setText(f"{numberOfBombs} left")
    numberOfBombsDisplay.setObjectName("numberOfBombsDisplay")
    numberOfBombsDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Update timer
    self.timer.timeout.connect(self.updateTimer)
    self.timerWidget.display(self.time.toString('mm:ss'))

    # Timer Widget
    self.timerWidget.setObjectName("timer")
    self.timerWidget.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)

    # Create possible coordinates for bombs to take sample of
    for i in range(self.gameBoardHeight):
      for j in range(self.gameBoardWidth):
        self.possibleCoordinates.append([j,i])

    # Create bomb coordinates
    self.bombCoordinates = random.sample(self.possibleCoordinates, numberOfBombs)
    
    # Create Bombs
    for i in range(len(self.bombCoordinates)):
      tileNumber = TileNumber(self.bombCoordinates[i][0],self.bombCoordinates[i][1],0,True)
      self.tileNumbers.append(tileNumber)
      gridLayout.addWidget(tileNumber.getTileNumber(), (tileNumber.y_pos), (tileNumber.x_pos))

    # Create number tiles and buttons
    for i in range(self.gameBoardHeight):
      for j in range(self.gameBoardWidth):
        adjacentBombs = 0
        if ([j,i] not in self.bombCoordinates):
          for bomb in self.bombCoordinates:
            if (i-1 == bomb[1] or i+1 == bomb[1] or i == bomb[1]) and (j-1 == bomb[0] or j+1 == bomb[0] or j == bomb[0]): 
              adjacentBombs += 1
          tileNumber = TileNumber(j,i,adjacentBombs)
          self.tileNumbers.append(tileNumber)
          gridLayout.addWidget(tileNumber.getTileNumber(), (i), (j))
        tileButton = CustomButton(j,i,self.bombCoordinates)
        self.tileButtons.append(tileButton)
        gridLayout.addWidget(tileButton.getTileButton(), (i), (j))
        tileButton.clicked.connect(self.tileClick)

    gridLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
    vertLayout.setAlignment(Qt.AlignmentFlag.AlignRight)

    horizLayout.addWidget(numberOfBombsDisplay)
    horizLayout.addWidget(self.timerWidget)
    vertLayout.addLayout(horizLayout)
    vertLayout.addLayout(gridLayout)
    widget.setLayout(vertLayout)
    self.setCentralWidget(widget)

  # Read tile click
  def tileClick(self):
    if (len(self.tileButtons) == self.gameBoardHeight * self.gameBoardWidth):
      self.startGame()
    clickedButton = self.sender()
    clickedButton.deleteLater()
    self.tileButtons.remove(clickedButton)

  # Start timer
  def startGame(self):
    self.timer.start(1000)

  # Update timer
  def updateTimer(self):
    self.time = self.time.addSecs(1)
    self.timerWidget.display(self.time.toString('mm:ss'))
    

app = QApplication(sys.argv)
app.setStyleSheet(Path('assets/styles/Styles.qss').read_text())

window = MainWindow()
window.show()

app.exec()