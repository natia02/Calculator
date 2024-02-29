import math

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtCore import Qt
from ResultWindow import ResultWindow


class ThirdWindow(QWidget):
    def __init__(self, figure, calculation, previous_window):
        super().__init__()
        self.previous_window = previous_window
        self.setWindowTitle("კალკულატორი")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.resize(385, 376)
        self.layout = QVBoxLayout()

        self.figure = figure
        self.calculation = calculation

        self.input_labels = []
        self.inputs = []

        self.setStyleSheet("""
                                          QWidget {
                                              background-color: rgb(163, 163, 163);
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

        self.label = QLabel(self)
        self.label.setText("შეიყვანეთ პარამეტრები")
        self.layout.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
                QLabel {
                     margin-top: 30px;
                     font-size: 25px;
               }
        """)

        if self.figure == "სამკუთხედი" and self.calculation == "ფართობი":
            self.input_labels = ["ფუძე:", "სიმაღლე:"]
        elif self.figure == "სამკუთხედი" and self.calculation == "პერიმეტრი":
            self.input_labels = ["გვერდი 1:", "გვერდი 2:", "გვერდი 3:"]
        elif self.figure == "მართკუთხედი":
            self.input_labels = ["სიგრძე:", "სიგანე:"]
        elif self.figure == "წრე":
            self.input_labels = ["რადიუსი:"]
        elif self.figure == "ტრაპეცია" and self.calculation == "პერიმეტრი":
            self.input_labels = ["ფუძე 1:", "ფუძე 2:", "ფერდი 1:", "ფერდი 2:"]
        elif self.figure == "ტრაპეცია" and self.calculation == "ფართობი":
            self.input_labels = ["ფუძე:", "სიმაღლე:"]

        for label in self.input_labels:
            label2 = QLabel(label)
            label2.setStyleSheet("""
                                QLabel{
                                    font-size: 15px;
                                }
                        """)
            self.layout.addWidget(label2)
            line_edit = QLineEdit()
            if label == "რადიუსი:":
                label2.setStyleSheet("""
                                                QLabel{
                                                    font-size: 15px;
                                                    margin-top:40px;
                                                }
                                        """)
                line_edit.setStyleSheet("""
                                    QLineEdit{
                                        padding: 10px, 10px;
                                        border-radius:10px;
                                        font-size: 15px;
                                        background-color: rgb(234, 234, 234);
                                        margin-bottom:60px !important;
                                    }
                            """)
            else:
                line_edit.setStyleSheet("""
                                    QLineEdit{
                                        padding: 10px, 10px;
                                        border-radius:10px;
                                        font-size: 15px;
                                        background-color: rgb(234, 234, 234);
                                    }
                            """)

            line_edit.setValidator(QDoubleValidator())
            self.inputs.append(line_edit)
            self.layout.addWidget(line_edit)

        self.calculate_button = QPushButton("გამოთვლა")
        self.calculate_button.clicked.connect(self.calculate)
        self.layout.addWidget(self.calculate_button)

        self.back_button = QPushButton("უკან")
        self.back_button.clicked.connect(self.goBack)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def calculate(self):
        values = []
        for line_edit in self.inputs:
            value = line_edit.text()
            print(value)
            if value:
                try:
                    values.append(float(value))
                except ValueError:
                    self.result_window = ResultWindow("Error: გთხოვთ შეიყვანოთ ვალიდური რიცხვი", self.figure,
                                                      self.calculation, self)
                    self.close()
                    self.result_window.show()
                    return
            else:
                self.result_window = ResultWindow("Error: გთხოვთ შეავსოთ ფილდები", self.figure, self.calculation,
                                                  self)
                self.close()
                self.result_window.show()
                return

        if self.figure == "სამკუთხედი":
            if self.calculation == "ფართობი":
                self.close()
                area = 0.5 * values[0] * values[1]
                self.result_window = ResultWindow(f"ფართობი: {area} სმ", self.figure, self.calculation, self)
                self.result_window.show()
            elif self.calculation == "პერიმეტრი":
                self.close()
                parameter = sum(values)
                self.result_window = ResultWindow(f"პერიმეტრი: {parameter} სმ", self.figure, self.calculation, self)
                self.result_window.show()
        elif self.figure == "მართკუთხედი":
            if self.calculation == "ფართობი":
                self.close()
                area = values[0] * values[1]
                self.result_window = ResultWindow(f"ფართობი: {area} სმ", self.figure, self.calculation, self)
                self.result_window.show()
            elif self.calculation == "პერიმეტრი":
                self.close()
                parameter = sum(values) * 2
                self.result_window = ResultWindow(f"პერიმეტრი: {parameter} სმ", self.figure, self.calculation, self)
                self.result_window.show()
        elif self.figure == "წრე":
            if self.calculation == "ფართობი":
                self.close()
                area = 2 * math.pi * math.pow(values[0], 2)
                self.result_window = ResultWindow(f"ფართობი: {area} სმ", self.figure, self.calculation, self)
                self.result_window.show()
            elif self.calculation == "პერიმეტრი":
                self.close()
                parameter = 2 * math.pi * values[0]
                self.result_window = ResultWindow(f"სიგრძე: {parameter} სმ", self.figure, self.calculation, self)
                self.result_window.show()
        elif self.figure == "ტრაპეცია":
            if self.calculation == "ფართობი":
                self.close()
                area = values[0] * values[1]
                self.result_window = ResultWindow(f"ფართობი: {area} სმ", self.figure, self.calculation, self)
                self.result_window.show()
            elif self.calculation == "პერიმეტრი":
                self.close()
                parameter = sum(values)
                self.result_window = ResultWindow(f"პერიმეტრი: {parameter} სმ", self.figure, self.calculation, self)
                self.result_window.show()


    def goBack(self):
        self.close()
        self.previous_window.show()
