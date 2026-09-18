# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 477)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.topic_comboBox = QComboBox(self.centralwidget)
        self.topic_comboBox.addItem("")
        self.topic_comboBox.addItem("")
        self.topic_comboBox.addItem("")
        self.topic_comboBox.addItem("")
        self.topic_comboBox.setObjectName(u"topic_comboBox")
        self.topic_comboBox.setGeometry(QRect(10, 70, 531, 22))
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(240, 0, 64, 16))
        self.topic_label = QLabel(self.centralwidget)
        self.topic_label.setObjectName(u"topic_label")
        self.topic_label.setGeometry(QRect(10, 50, 80, 16))
        self.show_button = QPushButton(self.centralwidget)
        self.show_button.setObjectName(u"show_button")
        self.show_button.setGeometry(QRect(30, 100, 491, 41))
        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(10, 170, 531, 251))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.topic_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0637\u0646\u0632", None))
        self.topic_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0627\u0646\u06af\u06cc\u0632\u0634\u06cc", None))
        self.topic_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0627\u062d\u0633\u0627\u0633\u06cc", None))
        self.topic_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0634\u0639\u0631", None))

        self.title_label.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0645\u0644\u0647 \u06cc \u0627\u0645\u0631\u0648\u0632", None))
        self.topic_label.setText(QCoreApplication.translate("MainWindow", u": \u0627\u0646\u062a\u062e\u0627\u0628 \u0645\u0648\u0636\u0648\u0639", None))
        self.show_button.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0645\u0627\u06cc\u0634 \u062c\u0645\u0644\u0647", None))
        self.result_label.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0645\u0644\u0647 \u0627\u06cc\u0646\u062c\u0627 \u0646\u0645\u0627\u06cc\u0634 \u062f\u0627\u062f\u0647 \u0645\u06cc\u0634\u0648\u062f", None))
    # retranslateUi

