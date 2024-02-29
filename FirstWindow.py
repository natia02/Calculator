import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QLineEdit, \
    QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from SecondWindow import SecondWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("კალკულატორი")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.resize(385, 376)
        self.layout = QVBoxLayout()
        self.setStyleSheet("""
                    QWidget {
                        background-color: rgb(163, 163, 163);
                    }
                    QLabel {
                        margin-left:80px;
                        font-size: 25px;
                        margin-bottom: 30px;
                    }
                    QRadioButton {
                        padding-top: 10px;
                        font-size: 16px;
                    }
                    QPushButton {
                        font-size: 15px;
                        background-color: #007bff;
                        color: #ffffff;
                        border: none;
                        padding: 8px 16px;
                        border-radius: 10px;
                        margin-top: 30px;
                    }
                    QPushButton:hover {
                        background-color: #0056b3;
                    }
                """)

        self.figure_radio_buttons = []
        self.figure_radio_button_names = ["სამკუთხედი", "მართკუთხედი", "წრე", "ტრაპეცია"]

        self.figure_selection_label = QLabel("აირჩიე ფიგურა")
        self.figure_selection_label.setAlignment((Qt.AlignVCenter))
        self.layout.addWidget(self.figure_selection_label)

        for name in self.figure_radio_button_names:
            rb = QRadioButton(name)
            self.figure_radio_buttons.append(rb)
            self.layout.addWidget(rb)

        self.submit_button = QPushButton("არჩევა")
        self.submit_button.clicked.connect(self.showSecondWindow)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def showSecondWindow(self):
        selected_figure = ""
        for rb in self.figure_radio_buttons:
            if rb.isChecked():
                selected_figure = rb.text()
                break

        if selected_figure:
            self.second_window = SecondWindow(selected_figure, self)
            self.second_window.show()
            self.hide()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
