from PyQt6.QtWidgets import (
  QWidget,
  QPushButton
)

class TileButton:
  def __init__(self, x_pos, y_pos):
    self.x_pos = x_pos
    self.y_pos = y_pos

    self.tileButton = QPushButton(f"{self.x_pos}, {self.y_pos}")
    self.tileButton.setFixedSize(50,50)
    self.tileButton.clicked.connect(self.revealTile)
  
  def getTileButton(self):
    return self.tileButton
  
  def revealTile(self):
    self.tileButton.deleteLater()