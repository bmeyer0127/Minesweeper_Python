from PyQt6.QtWidgets import (
  QWidget,
  QLCDNumber,
)

class TileNumber:
  def __init__(self, x_pos, y_pos):
    self.x_pos = x_pos
    self.y_pos = y_pos

    self.tileNumber = QLCDNumber()

  def getTileNumber(self):
    self.tileNumber.display(f"{self.x_pos},{self.y_pos}")
    self.tileNumber.setFixedSize(50,50)
    return self.tileNumber