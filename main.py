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
    # self.setFixedSize(QSize(600,500))

    def gameSetup():
      widget = QWidget()
      gridLayout = QGridLayout()
      self.startButtons = []
      self.time = QTime(0,0,0)
      self.timer = QTimer()
      self.timerWidget = QLCDNumber()
      self.numberOfBombsDisplay = QLabel()
      self.resetButton = QPushButton()
      self.exitButton = QPushButton()
      self.tileButtons = []
      self.tileNumbers = []
      self.numberCoordinates = []
      self.bombCoordinates = []
      self.numberOfBombs = 20
      self.numberOfBombsLeft = self.numberOfBombs
      self.gameBoardWidth = 10
      self.gameBoardHeight = 10
      self.possibleCoordinates = []

      # Number of bombs display widget
      self.numberOfBombsDisplay.setText(f"{self.numberOfBombsLeft} left")
      self.numberOfBombsDisplay.setObjectName("numberOfBombsDisplay")
      self.numberOfBombsDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)

      # Timer Widget
      self.timerWidget.setObjectName("timer")
      self.timerWidget.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)

      # Reset Button
      self.resetButton.setObjectName("resetButton")
      self.resetButton.setText("reset")
      self.resetButton.clicked.connect(gameSetup)

      # Exit Button
      self.exitButton.setObjectName("exitButton")
      self.exitButton.setText("exit")
      self.exitButton.clicked.connect(self.quitGame)

      # Update timer
      self.timer.timeout.connect(self.updateTimer)
      self.timerWidget.display(self.time.toString('mm:ss'))

      # Create possible coordinates for bombs to take sample of
      for i in range(self.gameBoardHeight):
        for j in range(self.gameBoardWidth):
          self.possibleCoordinates.append([j,i])

      # Create bomb coordinates
      self.bombCoordinates = random.sample(self.possibleCoordinates, self.numberOfBombs)
      
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
          tileButton.leftClicked.connect(self.leftTileClick)
          tileButton.rightClicked.connect(self.rightTileClick)

      gridLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

      self.leftButtonLayout = QVBoxLayout()
      self.leftButtonLayout.addWidget(self.resetButton)
      self.leftButtonLayout.addWidget(self.exitButton)
      self.leftButtonLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)

      self.topDisplayLayout = QHBoxLayout()
      self.topDisplayLayout.addWidget(self.numberOfBombsDisplay)
      self.topDisplayLayout.addWidget(self.timerWidget)

      self.rightSideLayout = QVBoxLayout()
      self.rightSideLayout.addLayout(self.topDisplayLayout)
      self.rightSideLayout.addLayout(gridLayout)

      self.mainLayout = QHBoxLayout()
      self.mainLayout.addLayout(self.leftButtonLayout)
      self.mainLayout.addLayout(self.rightSideLayout)

      widget.setLayout(self.mainLayout)
      self.setCentralWidget(widget)

    gameSetup()

  # Read left tile click
  def leftTileClick(self):
    print("left tile click")
    if (len(self.tileButtons) == self.gameBoardHeight * self.gameBoardWidth):
      self.startGame()
    clickedButton = self.sender()
    clickedButton.deleteLater()
    self.tileButtons.remove(clickedButton)

  # Read right tile click
  def rightTileClick(self):
    self.numberOfBombsLeft -= 1
    self.numberOfBombsDisplay.setText(f"{self.numberOfBombsLeft} left")

  # Start timer
  def startGame(self):
    self.timer.start(1000)

  # Quit game
  def quitGame(self):
    sys.exit()

  # Update timer
  def updateTimer(self):
    self.time = self.time.addSecs(1)
    self.timerWidget.display(self.time.toString('mm:ss'))
    
  # End game either on bomb click or all non-bomb tiles cleared
  def endGame(self):
    print("endGame")
  

app = QApplication(sys.argv)
app.setStyleSheet(Path('assets/styles/Styles.qss').read_text())

window = MainWindow()
window.show()

app.exec()