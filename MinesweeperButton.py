from PyQt6.QtWidgets import (
  QWidget,
  QPushButton
)

class TileButton:
  def __init__(self, x_pos, y_pos):
    self.x_pos = x_pos
    self.y_pos = y_pos
  
  def getTileButton(self):
    return QPushButton(f"{self.x_pos}, {self.y_pos}")