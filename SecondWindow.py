from PyQt5.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from ThirdWindow import ThirdWindow


class SecondWindow(QWidget):
    def __init__(self, figure, previous_window):
        super().__init__()
        self.previous_window = previous_window
        self.setWindowTitle("კალკულატორი")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.resize(385, 376)
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("""
                                   QWidget {
                                       background-color: rgb(163, 163, 163);
                                   }
                                   QLabel {
                                       margin-top: 30px;
                                       font-size: 25px;
                                   }
                                   
                                   QRadioButton {
                                       padding-top:20px;
                                       font-size: 16px;
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
        self.figure = figure

        self.calculation_label = QLabel("აირჩიე რისი გამოთვლა გინდა")
        self.layout.addWidget(self.calculation_label)

        self.area_radio_button = QRadioButton("ფართობი")
        self.area_radio_button.setStyleSheet("""
        QRadioButton {
            margin-top:50px;
        }
        """)
        self.layout.addWidget(self.area_radio_button)

        self.parameter_radio_button = QRadioButton("პერიმეტრი")
        self.layout.addWidget(self.parameter_radio_button)

        self.submit_button = QPushButton("არჩევა")
        self.submit_button.setStyleSheet("""
             QPushButton {
               margin-top:50px;
            }
        """)
        self.submit_button.clicked.connect(self.showThirdWindow)
        self.layout.addWidget(self.submit_button)

        self.back_button = QPushButton("უკან")
        self.back_button.clicked.connect(self.goBack)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def showThirdWindow(self):
        selected_calculation = ""
        if self.area_radio_button.isChecked():
            selected_calculation = "ფართობი"
        elif self.parameter_radio_button.isChecked():
            selected_calculation = "პერიმეტრი"

        if selected_calculation:
            self.third_window = ThirdWindow(self.figure, selected_calculation, self)
            self.third_window.show()
            self.hide()

    def goBack(self):
        self.close()
        self.previous_window.show()
