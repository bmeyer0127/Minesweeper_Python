from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import (
  QWidget,
  QLCDNumber,
  QLabel,
)

class TileNumber:
  def __init__(self, x_pos, y_pos, adjacentBombs=0, isBomb=False):
    self.bombIcon = QPixmap("assets/bomb.svg")
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.adjacentBombs = adjacentBombs
    self.isBomb = isBomb

    # self.tileNumber = QLCDNumber()
    self.tileNumber = QLabel()

  def getTileNumber(self):
    if self.isBomb:
      self.tileNumber.setText("BOMB")
    else:
      self.tileNumber.setText(f"{self.adjacentBombs}")
    self.tileNumber.setFixedSize(50,50)
    return self.tileNumber