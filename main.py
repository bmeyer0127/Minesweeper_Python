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
    bombCoordinates = []

    self.setWindowTitle("MineSweeper")
    self.setFixedSize(QSize(600,500))

    widget = QWidget()
    gameBoardWidget = QWidget()
    gridLayout = QGridLayout()
    horizLayout = QHBoxLayout()
    vertLayout = QVBoxLayout()
    self.tileButtons = []
    self.tileNumbers = []
    self.numberCoordinates = []
    self.bombCoordinates = []
    numberOfBombs = 20
    gameBoardWidth = 10
    gameBoardHeight = 10
    self.possibleCoordinates = []

    # Number of bombs display widget
    numberOfBombsDisplay = QLabel()
    numberOfBombsDisplay.setText(f"{numberOfBombs} left")
    numberOfBombsDisplay.setObjectName("numberOfBombsDisplay")
    numberOfBombsDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Create timer
    timer = QTimer(widget)
    timer.timeout.connect(updateTimer)

    # Timer Widget
    timerWidget = QLCDNumber()
    timerWidget.setObjectName("timer")
    # timerWidget.display("5233")
    timerWidget.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)

    # Update timer
    def updateTimer():
      currentTime = QTime.currentTime()
      timerWidget.display(currentTime.toString('HH:mm:ss'))

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
          tileNumber = TileNumber(j,i,adjacentBombs)
          self.tileNumbers.append(tileNumber)
          gridLayout.addWidget(tileNumber.getTileNumber(), (i), (j))
        tileButton = CustomButton(j,i,self.bombCoordinates)
        self.tileButtons.append(tileButton)
        gridLayout.addWidget(tileButton.getTileButton(), (i), (j))

    gridLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
    vertLayout.setAlignment(Qt.AlignmentFlag.AlignRight)

    horizLayout.addWidget(numberOfBombsDisplay)
    horizLayout.addWidget(timerWidget)
    vertLayout.addLayout(horizLayout)
    vertLayout.addLayout(gridLayout)
    # vertLayout.addLayout(horizLayout)
    widget.setLayout(vertLayout)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)
app.setStyleSheet(Path('assets/styles/Styles.qss').read_text())

window = MainWindow()
window.show()

app.exec()