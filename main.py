from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])

window = QWidget(windowTitle="Hello World")
window.show()

app.exec()