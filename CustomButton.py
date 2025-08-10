from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap

class CustomButton(QPushButton):
  def __init__(self, x_pos, y_pos):
    super().__init__()
    self.flagIcon = QPixmap("assets/flag.svg")

    self.x_pos = x_pos
    self.y_pos = y_pos
    self.setText(f"{self.x_pos}, {self.y_pos}")
    self.setFixedSize(50,50)

  def getTileButton(self):
    return self

  def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
      print("left")
      self.revealTile()
    elif event.button() == Qt.MouseButton.RightButton:
      print("right")
      self.setFlag()

  def revealTile(self):
    self.deleteLater()

  def setFlag(self):
    self.setIcon(QIcon(self.flagIcon))