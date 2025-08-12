from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
import time

class CustomButton(QPushButton):
  def __init__(self, x_pos, y_pos, bombCoordinates):
    super().__init__()
    self.flagIcon = QPixmap("assets/flag.svg")
    self.hasFlag = False

    self.x_pos = x_pos
    self.y_pos = y_pos
    self.bombCoordinates = bombCoordinates
    self.setFixedSize(50,50)
    self.setObjectName("customButton")

  def getTileButton(self):
    return self

  def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
      if not self.hasFlag:
        self.revealTile(self.bombCoordinates)
    elif event.button() == Qt.MouseButton.RightButton:
      self.toggleFlag()

  def revealTile(self, bombCoordinates):
    self.deleteLater()
    print("poop")
    print(bombCoordinates)
    for coord in bombCoordinates:
      if self.x_pos == coord[0] and self.y_pos == coord[1]:
        print(f"x:{self.x_pos}, y:{self.y_pos}, bombx:{coord[0]}, bomby:{coord[1]}")
        print("Mega death")

  def toggleFlag(self):
    self.hasFlag = not self.hasFlag
    if self.hasFlag:
      self.setIcon(QIcon(self.flagIcon))
    else:
      self.setIcon(QIcon(None))