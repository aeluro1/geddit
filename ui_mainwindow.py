# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gedditYHvXAO.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(218, 224, 230);")
        self.actionAuthentication = QAction(MainWindow)
        self.actionAuthentication.setObjectName(u"actionAuthentication")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.body = QFrame(self.centralWidget)
        self.body.setObjectName(u"body")
        self.body.setFrameShape(QFrame.NoFrame)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.body)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameSideMenu = QFrame(self.body)
        self.frameSideMenu.setObjectName(u"frameSideMenu")
        self.frameSideMenu.setMinimumSize(QSize(70, 0))
        self.frameSideMenu.setMaximumSize(QSize(70, 16777215))
        self.frameSideMenu.setStyleSheet(u"background-color: rgb(95, 153, 207);")
        self.frameSideMenu.setFrameShape(QFrame.NoFrame)
        self.frameSideMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameSideMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameNav = QFrame(self.frameSideMenu)
        self.frameNav.setObjectName(u"frameNav")
        self.frameNav.setFrameShape(QFrame.NoFrame)
        self.frameNav.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameNav)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnPageHome = QPushButton(self.frameNav)
        self.btnPageHome.setObjectName(u"btnPageHome")
        self.btnPageHome.setMinimumSize(QSize(0, 40))
        self.btnPageHome.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 121, 211);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(206, 227, 248);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnPageHome)

        self.btnPageDownload = QPushButton(self.frameNav)
        self.btnPageDownload.setObjectName(u"btnPageDownload")
        self.btnPageDownload.setMinimumSize(QSize(0, 40))
        self.btnPageDownload.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 121, 211);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(206, 227, 248);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnPageDownload)

        self.btnPageSettings = QPushButton(self.frameNav)
        self.btnPageSettings.setObjectName(u"btnPageSettings")
        self.btnPageSettings.setMinimumSize(QSize(0, 40))
        self.btnPageSettings.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 121, 211);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(206, 227, 248);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnPageSettings)


        self.verticalLayout_3.addWidget(self.frameNav)

        self.pushButton = QPushButton(self.frameSideMenu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 121, 211);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(206, 227, 248);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.frameSideMenu)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 69, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frameSideMenu)

        self.framePagesContainer = QFrame(self.body)
        self.framePagesContainer.setObjectName(u"framePagesContainer")
        self.framePagesContainer.setFrameShape(QFrame.NoFrame)
        self.framePagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.framePagesContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widgetPages = QStackedWidget(self.framePagesContainer)
        self.widgetPages.setObjectName(u"widgetPages")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.widgetPages.addWidget(self.pageHome)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.widgetPages.addWidget(self.pageSettings)
        self.pageDownload = QWidget()
        self.pageDownload.setObjectName(u"pageDownload")
        self.widgetPages.addWidget(self.pageDownload)

        self.verticalLayout_5.addWidget(self.widgetPages)


        self.horizontalLayout_2.addWidget(self.framePagesContainer)


        self.verticalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAuthentication.setText(QCoreApplication.translate("MainWindow", u"Authentication", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btnPageHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btnPageDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.btnPageSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Geddit v1.0", None))
    # retranslateUi