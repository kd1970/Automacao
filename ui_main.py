# -*- coding: utf-8 -*-
import sys 
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QAction,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,QMenu, QSystemTrayIcon,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QTextBrowser, QTextEdit, QWidget)


class Ui_MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(Ui_MainWindow, self).__init__()
        self.show()
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 600)
        MainWindow.setMinimumSize(QSize(820, 600))
        MainWindow.setMaximumSize(QSize(820, 600))
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(820, 600))
        self.centralwidget.setMaximumSize(QSize(820, 600))
        self.centralwidget.setStyleSheet(u"alternate-background-color: rgb(77, 92, 147);\n"
"opacity: 0.5;")
        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(20, 250, 160, 321))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BtnPrivt2 = QPushButton(self.gridLayoutWidget_3)
        self.BtnPrivt2.setObjectName(u"BtnPrivt2")

        self.gridLayout_3.addWidget(self.BtnPrivt2, 2, 0, 1, 1)

        self.BtnPrivt4 = QPushButton(self.gridLayoutWidget_3)
        self.BtnPrivt4.setObjectName(u"BtnPrivt4")

        self.gridLayout_3.addWidget(self.BtnPrivt4, 4, 0, 1, 1)

        self.BtnPrivt6 = QPushButton(self.gridLayoutWidget_3)
        self.BtnPrivt6.setObjectName(u"BtnPrivt6")

        self.gridLayout_3.addWidget(self.BtnPrivt6, 7, 0, 1, 1)

        self.BtnPrivt1 = QPushButton(self.gridLayoutWidget_3)
        self.BtnPrivt1.setObjectName(u"BtnPrivt1")
        self.BtnPrivt1.setAutoFillBackground(True)
        self.BtnPrivt1.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.BtnPrivt1, 1, 0, 1, 1)

        self.BtnPrivt7 = QPushButton(self.gridLayoutWidget_3)
        self.BtnPrivt7.setObjectName(u"BtnPrivt7")

        self.gridLayout_3.addWidget(self.BtnPrivt7, 8, 0, 1, 1)

        self.BtnPrivt5 = QPushButton(self.gridLayoutWidget_3)
        self.BtnPrivt5.setObjectName(u"BtnPrivt5")

        self.gridLayout_3.addWidget(self.BtnPrivt5, 6, 0, 1, 1)

        self.BtnPrivt9 = QPushButton(self.gridLayoutWidget_3)
        self.BtnPrivt9.setObjectName(u"BtnPrivt9")

        self.gridLayout_3.addWidget(self.BtnPrivt9, 10, 0, 1, 1)

        self.BtnPrivt8 = QPushButton(self.gridLayoutWidget_3)
        self.BtnPrivt8.setObjectName(u"BtnPrivt8")

        self.gridLayout_3.addWidget(self.BtnPrivt8, 9, 0, 1, 1)

        self.BtnPrivt3 = QPushButton(self.gridLayoutWidget_3)
        self.BtnPrivt3.setObjectName(u"BtnPrivt3")

        self.gridLayout_3.addWidget(self.BtnPrivt3, 3, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 230, 91, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 230, 101, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 230, 81, 20))
        self.gridLayoutWidget_4 = QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(200, 250, 160, 321))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BtnMig8 = QPushButton(self.gridLayoutWidget_4)
        self.BtnMig8.setObjectName(u"BtnMig8")

        self.gridLayout_4.addWidget(self.BtnMig8, 10, 0, 1, 1)

        self.BtnMig3 = QPushButton(self.gridLayoutWidget_4)
        self.BtnMig3.setObjectName(u"BtnMig3")

        self.gridLayout_4.addWidget(self.BtnMig3, 4, 0, 1, 1)

        self.BtnMig5 = QPushButton(self.gridLayoutWidget_4)
        self.BtnMig5.setObjectName(u"BtnMig5")

        self.gridLayout_4.addWidget(self.BtnMig5, 7, 0, 1, 1)

        self.BtnMig6 = QPushButton(self.gridLayoutWidget_4)
        self.BtnMig6.setObjectName(u"BtnMig6")

        self.gridLayout_4.addWidget(self.BtnMig6, 8, 0, 1, 1)

        self.BtnMig4 = QPushButton(self.gridLayoutWidget_4)
        self.BtnMig4.setObjectName(u"BtnMig4")

        self.gridLayout_4.addWidget(self.BtnMig4, 5, 0, 1, 1)

        self.BtnMig2 = QPushButton(self.gridLayoutWidget_4)
        self.BtnMig2.setObjectName(u"BtnMig2")

        self.gridLayout_4.addWidget(self.BtnMig2, 3, 0, 1, 1)

        self.BtnMig7 = QPushButton(self.gridLayoutWidget_4)
        self.BtnMig7.setObjectName(u"BtnMig7")

        self.gridLayout_4.addWidget(self.BtnMig7, 9, 0, 1, 1)

        self.BtnMig9 = QPushButton(self.gridLayoutWidget_4)
        self.BtnMig9.setObjectName(u"BtnMig9")

        self.gridLayout_4.addWidget(self.BtnMig9, 11, 0, 1, 1)

        self.BtnMig1 = QPushButton(self.gridLayoutWidget_4)
        self.BtnMig1.setObjectName(u"BtnMig1")

        self.gridLayout_4.addWidget(self.BtnMig1, 2, 0, 1, 1)

        self.gridLayoutWidget_5 = QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(390, 250, 160, 321))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.BtnDasd7 = QPushButton(self.gridLayoutWidget_5)
        self.BtnDasd7.setObjectName(u"BtnDasd7")

        self.gridLayout_5.addWidget(self.BtnDasd7, 11, 0, 1, 1)

        self.BtnDasd3 = QPushButton(self.gridLayoutWidget_5)
        self.BtnDasd3.setObjectName(u"BtnDasd3")

        self.gridLayout_5.addWidget(self.BtnDasd3, 4, 0, 1, 1)

        self.BtnDasd1 = QPushButton(self.gridLayoutWidget_5)
        self.BtnDasd1.setObjectName(u"BtnDasd1")
        self.BtnDasd1.setStyleSheet(u"")
        self.BtnDasd1.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.BtnDasd1, 1, 0, 1, 1)

        self.BtnDasd2 = QPushButton(self.gridLayoutWidget_5)
        self.BtnDasd2.setObjectName(u"BtnDasd2")

        self.gridLayout_5.addWidget(self.BtnDasd2, 3, 0, 1, 1)

        self.BtnDasd5 = QPushButton(self.gridLayoutWidget_5)
        self.BtnDasd5.setObjectName(u"BtnDasd5")

        self.gridLayout_5.addWidget(self.BtnDasd5, 8, 0, 1, 1)

        self.BtnDasd6 = QPushButton(self.gridLayoutWidget_5)
        self.BtnDasd6.setObjectName(u"BtnDasd6")

        self.gridLayout_5.addWidget(self.BtnDasd6, 9, 0, 1, 1)

        self.BtnDasd9 = QPushButton(self.gridLayoutWidget_5)
        self.BtnDasd9.setObjectName(u"BtnDasd9")

        self.gridLayout_5.addWidget(self.BtnDasd9, 13, 0, 1, 1)

        self.BtnDasd4 = QPushButton(self.gridLayoutWidget_5)
        self.BtnDasd4.setObjectName(u"BtnDasd4")

        self.gridLayout_5.addWidget(self.BtnDasd4, 6, 0, 1, 1)

        self.BtnDasd8 = QPushButton(self.gridLayoutWidget_5)
        self.BtnDasd8.setObjectName(u"BtnDasd8")

        self.gridLayout_5.addWidget(self.BtnDasd8, 12, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -1, 820, 600))
        self.frame.setMinimumSize(QSize(820, 600))
        self.frame.setMaximumSize(QSize(800, 600))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayoutWidget_6 = QWidget(self.frame)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(610, 480, 181, 81))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.BtnDasd = QPushButton(self.gridLayoutWidget_6)
        self.BtnDasd.setObjectName(u"BtnDasd")
        self.BtnDasd.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.gridLayout_6.addWidget(self.BtnDasd, 4, 0, 1, 1)

        self.BtnMig = QPushButton(self.gridLayoutWidget_6)
        self.BtnMig.setObjectName(u"BtnMig")
        self.BtnMig.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.gridLayout_6.addWidget(self.BtnMig, 2, 0, 1, 1)

        self.BtnOff = QPushButton(self.gridLayoutWidget_6)
        self.BtnOff.setObjectName(u"BtnOff")
        self.BtnOff.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.gridLayout_6.addWidget(self.BtnOff, 4, 1, 1, 1)

        self.BtnPrivate = QPushButton(self.gridLayoutWidget_6)
        self.BtnPrivate.setObjectName(u"BtnPrivate")
        self.BtnPrivate.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.gridLayout_6.addWidget(self.BtnPrivate, 2, 1, 1, 1)

        self.TxtCriaTape = QLabel(self.gridLayoutWidget_6)
        self.TxtCriaTape.setObjectName(u"TxtCriaTape")

        self.gridLayout_6.addWidget(self.TxtCriaTape, 1, 0, 1, 2)

        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(610, 290, 182, 71))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(180, 25))
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1, Qt.AlignLeft)

        self.TxtLCD = QTextBrowser(self.gridLayoutWidget)
        self.TxtLCD.setObjectName(u"TxtLCD")
        self.TxtLCD.setMaximumSize(QSize(250, 50))
        self.TxtLCD.setStyleSheet(u"font: 9pt \"Courier New\";\n"
"background-color: qlineargradient(spread:pad, x1:0.483, y1:0.335, x2:1, y2:1, stop:0 rgba(250, 250, 250, 255), stop:1 rgba(215, 216, 207, 255));")

        self.gridLayout.addWidget(self.TxtLCD, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalSlider = QSlider(self.frame)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(570, 250, 16, 321))
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(610, 250, 181, 16))
        self.progressBar.setBaseSize(QSize(20, 20))
        palette = QPalette()
        brush = QBrush(QColor(181, 148, 148, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(77, 92, 147, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        self.progressBar.setPalette(palette)
        self.progressBar.setCursor(QCursor(Qt.WaitCursor))
        self.progressBar.setFocusPolicy(Qt.WheelFocus)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(181, 148, 148);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.136, x2:1, y2:0.125, stop:0.375 rgba(161, 179, 191, 255), stop:1 rgba(94, 133, 144, 255));\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(17, 10, 781, 201))
        self.textBrowser.setMaximumSize(QSize(850, 280))
        self.textBrowser.setLayoutDirection(Qt.LeftToRight)
        self.textBrowser.setStyleSheet(u"QTextBrowser{\n"
"	background-color: rgb(236, 236, 236);\n"
"font: 9pt \"SansSerif\";\n"
"font: 9pt \"Courier New\";\n"
"text-align: justify;\n"
"}")
        self.textBrowser.setFrameShape(QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QFrame.Sunken)
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textBrowser.setAutoFormatting(QTextEdit.AutoAll)
        self.gridLayoutWidget_2 = QWidget(self.frame)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(610, 410, 181, 31))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Mdriver = QLineEdit(self.gridLayoutWidget_2)
        self.Mdriver.setObjectName(u"Mdriver")
        self.Mdriver.setMaximumSize(QSize(40, 20))
        self.Mdriver.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"opacity: 0.5;")

        self.gridLayout_2.addWidget(self.Mdriver, 0, 1, 1, 1)

        self.BtnManual = QPushButton(self.gridLayoutWidget_2)
        self.BtnManual.setObjectName(u"BtnManual")
        self.BtnManual.setMaximumSize(QSize(40, 30))
        font = QFont()
        font.setPointSize(7)
        self.BtnManual.setFont(font)
        self.BtnManual.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_2.addWidget(self.BtnManual, 0, 3, 1, 1)

        self.Mtape = QLineEdit(self.gridLayoutWidget_2)
        self.Mtape.setObjectName(u"Mtape")
        self.Mtape.setMaximumSize(QSize(50, 20))
        self.Mtape.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"opacity: 0.5;")
        self.Mtape.setInputMethodHints(Qt.ImhUppercaseOnly)

        self.gridLayout_2.addWidget(self.Mtape, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(610, 380, 171, 31))
        self.label_5.setStyleSheet(u"font: 8pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.gridLayoutWidget_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.gridLayoutWidget_4.raise_()
        self.gridLayoutWidget_5.raise_()
        QWidget.setTabOrder(self.BtnPrivt1, self.BtnPrivt2)
        QWidget.setTabOrder(self.BtnPrivt2, self.BtnPrivt3)
        QWidget.setTabOrder(self.BtnPrivt3, self.BtnPrivt4)
        QWidget.setTabOrder(self.BtnPrivt4, self.BtnPrivt5)
        QWidget.setTabOrder(self.BtnPrivt5, self.BtnPrivt6)
        QWidget.setTabOrder(self.BtnPrivt6, self.BtnPrivt7)
        QWidget.setTabOrder(self.BtnPrivt7, self.BtnPrivt8)
        QWidget.setTabOrder(self.BtnPrivt8, self.BtnPrivt9)
        QWidget.setTabOrder(self.BtnPrivt9, self.BtnMig1)
        QWidget.setTabOrder(self.BtnMig1, self.BtnMig2)
        QWidget.setTabOrder(self.BtnMig2, self.BtnMig3)
        QWidget.setTabOrder(self.BtnMig3, self.BtnMig4)
        QWidget.setTabOrder(self.BtnMig4, self.BtnMig5)
        QWidget.setTabOrder(self.BtnMig5, self.BtnMig6)
        QWidget.setTabOrder(self.BtnMig6, self.BtnMig7)
        QWidget.setTabOrder(self.BtnMig7, self.BtnMig8)
        QWidget.setTabOrder(self.BtnMig8, self.BtnMig9)
        QWidget.setTabOrder(self.BtnMig9, self.BtnDasd1)
        QWidget.setTabOrder(self.BtnDasd1, self.BtnDasd2)
        QWidget.setTabOrder(self.BtnDasd2, self.BtnDasd3)
        QWidget.setTabOrder(self.BtnDasd3, self.BtnDasd4)
        QWidget.setTabOrder(self.BtnDasd4, self.BtnDasd5)
        QWidget.setTabOrder(self.BtnDasd5, self.BtnDasd6)
        QWidget.setTabOrder(self.BtnDasd6, self.BtnDasd7)
        QWidget.setTabOrder(self.BtnDasd7, self.BtnDasd8)
        QWidget.setTabOrder(self.BtnDasd8, self.BtnDasd9)
        QWidget.setTabOrder(self.BtnDasd9, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.progressBar)
        QWidget.setTabOrder(self.progressBar, self.TxtLCD)
        QWidget.setTabOrder(self.TxtLCD, self.Mtape)
        QWidget.setTabOrder(self.Mtape, self.Mdriver)
        QWidget.setTabOrder(self.Mdriver, self.BtnManual)
        QWidget.setTabOrder(self.BtnManual, self.BtnMig)
        QWidget.setTabOrder(self.BtnMig, self.BtnPrivate)
        QWidget.setTabOrder(self.BtnPrivate, self.BtnDasd)
        QWidget.setTabOrder(self.BtnDasd, self.BtnOff)
        QWidget.setTabOrder(self.BtnOff, self.textBrowser)

        self.retranslateUi(MainWindow)
        self.BtnOff.clicked.connect(MainWindow.close)
        self.progressBar.valueChanged.connect(self.textBrowser.forward)
        self.textBrowser.cursorPositionChanged.connect(self.progressBar._raise)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TS3500", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.BtnPrivt2.setText(QCoreApplication.translate("MainWindow", u"A23031", None))
        self.BtnPrivt4.setText(QCoreApplication.translate("MainWindow", u"A23033", None))
        self.BtnPrivt6.setText(QCoreApplication.translate("MainWindow", u"A23035", None))
        self.BtnPrivt1.setText(QCoreApplication.translate("MainWindow", u"A23030", None))
        self.BtnPrivt7.setText(QCoreApplication.translate("MainWindow", u"A23036", None))
        self.BtnPrivt5.setText(QCoreApplication.translate("MainWindow", u"A23034", None))
        self.BtnPrivt9.setText(QCoreApplication.translate("MainWindow", u"A23039", None))
        self.BtnPrivt8.setText(QCoreApplication.translate("MainWindow", u"A23038", None))
        self.BtnPrivt3.setText(QCoreApplication.translate("MainWindow", u"A23032", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; vertical-align:super;\">Fitas HSM PRIVATE</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">PRIVATE TAPES</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; vertical-align:super;\">Fitas HSM PRIVATE</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">MIGRATE TAPES</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; vertical-align:super;\">Fitas HSM PRIVATE</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">DASD TAPES</p></body></html>", None))
        self.BtnMig8.setText(QCoreApplication.translate("MainWindow", u"MIG007", None))
        self.BtnMig3.setText(QCoreApplication.translate("MainWindow", u"MIG002", None))
        self.BtnMig5.setText(QCoreApplication.translate("MainWindow", u"MIG004", None))
        self.BtnMig6.setText(QCoreApplication.translate("MainWindow", u"MIG005", None))
        self.BtnMig4.setText(QCoreApplication.translate("MainWindow", u"MIG003", None))
        self.BtnMig2.setText(QCoreApplication.translate("MainWindow", u"MIG001", None))
        self.BtnMig7.setText(QCoreApplication.translate("MainWindow", u"MIG006", None))
        self.BtnMig9.setText(QCoreApplication.translate("MainWindow", u"MIG008", None))
        self.BtnMig1.setText(QCoreApplication.translate("MainWindow", u"MIG000", None))
        self.BtnDasd7.setText(QCoreApplication.translate("MainWindow", u"A00006", None))
        self.BtnDasd3.setText(QCoreApplication.translate("MainWindow", u"A00002", None))
#if QT_CONFIG(whatsthis)
        self.BtnDasd1.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.BtnDasd1.setText(QCoreApplication.translate("MainWindow", u"A00000", None))
        self.BtnDasd2.setText(QCoreApplication.translate("MainWindow", u"A00001", None))
        self.BtnDasd5.setText(QCoreApplication.translate("MainWindow", u"A00004", None))
        self.BtnDasd6.setText(QCoreApplication.translate("MainWindow", u"A00005", None))
        self.BtnDasd9.setText(QCoreApplication.translate("MainWindow", u"A00008", None))
        self.BtnDasd4.setText(QCoreApplication.translate("MainWindow", u"A00003", None))
        self.BtnDasd8.setText(QCoreApplication.translate("MainWindow", u"A00007", None))
        self.BtnDasd.setText(QCoreApplication.translate("MainWindow", u"DASD", None))
        self.BtnMig.setText(QCoreApplication.translate("MainWindow", u"Migrate", None))
        self.BtnOff.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.BtnPrivate.setText(QCoreApplication.translate("MainWindow", u"Private", None))
        self.TxtCriaTape.setText(QCoreApplication.translate("MainWindow", u"Cadastrar novas fitas  ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mount Tape Status", None))
        self.progressBar.setFormat("")
        self.Mdriver.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Driver", None))
        self.BtnManual.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.Mtape.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fita", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Informe o volser e driver da fita.", None))
    # retranslateUi

def LoadRobo():
    
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()

   # Create the icon
    icon = QIcon("pc.ico")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Create the menu
    menu = QMenu()
    action = QAction("Exibir")
    action.triggered.connect(lambda:window.showNormal())
    menu.addAction(action)

    # Add a Quit option to the menu.
    quit = QAction("Sair")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    app.exec()

LoadRobo()