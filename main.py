import sys
import sqlite3
import random

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection = sqlite3.connect("SQL.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT quote FROM quotes")
        self.quotes = self.cursor.fetchall()
        self.ui.show_button.clicked.connect(self.show_quote)

    def show_quote(self):
        topic = self.ui.topic_comboBox.currentText()
        self.cursor.execute("SELECT quote FROM quotes WHERE topic = ?", (topic,))
        quotes = self.cursor.fetchall()

        if quotes:
            quote = random.choice(quotes)
            self.ui.result_label.setText(quote[0])
        else:
            self.ui.result_label.setText("No quote found.")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())