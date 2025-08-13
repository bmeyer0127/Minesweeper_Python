from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize
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
    self.tileNumber = QLabel()
    self.tileNumber.setObjectName("tileNumber")
    # self.tileNumber.setFixedSize(80,80)
    self.tileNumber.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

  def getTileNumber(self):
    self.tileNumber.setText(None)
    if self.isBomb:
      # self.tileNumber.setText("BOMB")
      self.tileNumber.setPixmap(self.bombIcon)

    elif not self.isBomb:
      self.tileNumber.setText(f"{self.adjacentBombs}")
    return self.tileNumber