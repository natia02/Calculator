from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class ResultWindow(QWidget):
    def __init__(self, result, figure, calculation, previous_window):
        super().__init__()
        self.previous_window = previous_window
        self.setWindowTitle("Geometry Calculator - Result")
        self.setWindowTitle("კალკულატორი")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.resize(385, 376)
        self.layout = QVBoxLayout()

        self.setStyleSheet("""
                                           QWidget {
                                               background-color: rgb(163, 163, 163);
                                           }
                                           QLabel {
                                               font-size: 25px;
                                           }
                                           QPushButton {
                                                font-size: 15px;
                                                background-color: #007bff;
                                                color: #ffffff;
                                                border: none;
                                                padding: 8px 16px;
                                                border-radius: 10px;
                                           }
                                           QPushButton:hover {
                                                background-color: #0056b3;
                                           }
                                       """)

        self.result_label = QLabel(result)
        self.layout.addWidget(self.result_label)
        self.result_label.setAlignment(Qt.AlignVCenter)

        self.back_button = QPushButton("უკან")
        self.back_button.clicked.connect(self.goBack)
        self.layout.addWidget(self.back_button)

        self.figure = figure
        self.calculation = calculation

        self.setLayout(self.layout)

    def goBack(self):
        self.close()
        self.previous_window.show()