# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gedditpDkNAD.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QColumnView, QDateTimeEdit, QFormLayout,
    QFrame, QGraphicsView, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTreeView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(650, 400))
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
        self.frameSideMenu.setStyleSheet(u"QFrame#frameSideMenu {\n"
"	background-color: #5f99cf;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color: #0079d3;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #cee3f8;\n"
"}\n"
"\n"
"QLabel#labelGeddit {\n"
"	color: #ff4500;\n"
"}")
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
        self.btnPageHome.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnPageHome)

        self.btnPageDownload = QPushButton(self.frameNav)
        self.btnPageDownload.setObjectName(u"btnPageDownload")
        self.btnPageDownload.setMinimumSize(QSize(0, 40))
        self.btnPageDownload.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnPageDownload)

        self.btnPageSettings = QPushButton(self.frameNav)
        self.btnPageSettings.setObjectName(u"btnPageSettings")
        self.btnPageSettings.setMinimumSize(QSize(0, 40))
        self.btnPageSettings.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnPageSettings)

        self.btnPageAbout = QPushButton(self.frameNav)
        self.btnPageAbout.setObjectName(u"btnPageAbout")
        self.btnPageAbout.setMinimumSize(QSize(0, 40))
        self.btnPageAbout.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnPageAbout)


        self.verticalLayout_3.addWidget(self.frameNav)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.labelGeddit = QLabel(self.frameSideMenu)
        self.labelGeddit.setObjectName(u"labelGeddit")
        self.labelGeddit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelGeddit)


        self.horizontalLayout_2.addWidget(self.frameSideMenu)

        self.framePagesContainer = QFrame(self.body)
        self.framePagesContainer.setObjectName(u"framePagesContainer")
        self.framePagesContainer.setFrameShape(QFrame.NoFrame)
        self.framePagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.framePagesContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.widgetPages = QStackedWidget(self.framePagesContainer)
        self.widgetPages.setObjectName(u"widgetPages")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.verticalLayout_6 = QVBoxLayout(self.pageHome)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frameSearchContainer = QFrame(self.pageHome)
        self.frameSearchContainer.setObjectName(u"frameSearchContainer")
        self.frameSearchContainer.setFrameShape(QFrame.NoFrame)
        self.frameSearchContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameSearchContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameSearch = QFrame(self.frameSearchContainer)
        self.frameSearch.setObjectName(u"frameSearch")
        self.frameSearch.setMinimumSize(QSize(400, 0))
        self.frameSearch.setMaximumSize(QSize(400, 16777215))
        self.frameSearch.setFrameShape(QFrame.NoFrame)
        self.frameSearch.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameSearch)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 0, 0)
        self.formSearch = QFormLayout()
        self.formSearch.setObjectName(u"formSearch")
        self.formSearch.setHorizontalSpacing(20)
        self.formSearch.setVerticalSpacing(6)
        self.formSearch.setContentsMargins(0, 0, -1, -1)
        self.lineEditTitle = QLineEdit(self.frameSearch)
        self.lineEditTitle.setObjectName(u"lineEditTitle")

        self.formSearch.setWidget(0, QFormLayout.FieldRole, self.lineEditTitle)

        self.labelSubreddit = QLabel(self.frameSearch)
        self.labelSubreddit.setObjectName(u"labelSubreddit")

        self.formSearch.setWidget(1, QFormLayout.LabelRole, self.labelSubreddit)

        self.lineEditSubreddit = QLineEdit(self.frameSearch)
        self.lineEditSubreddit.setObjectName(u"lineEditSubreddit")

        self.formSearch.setWidget(1, QFormLayout.FieldRole, self.lineEditSubreddit)

        self.labelAuthor = QLabel(self.frameSearch)
        self.labelAuthor.setObjectName(u"labelAuthor")

        self.formSearch.setWidget(2, QFormLayout.LabelRole, self.labelAuthor)

        self.lineEditAuthor = QLineEdit(self.frameSearch)
        self.lineEditAuthor.setObjectName(u"lineEditAuthor")

        self.formSearch.setWidget(2, QFormLayout.FieldRole, self.lineEditAuthor)

        self.labelDateMin = QLabel(self.frameSearch)
        self.labelDateMin.setObjectName(u"labelDateMin")

        self.formSearch.setWidget(3, QFormLayout.LabelRole, self.labelDateMin)

        self.timeDateMin = QDateTimeEdit(self.frameSearch)
        self.timeDateMin.setObjectName(u"timeDateMin")

        self.formSearch.setWidget(3, QFormLayout.FieldRole, self.timeDateMin)

        self.labelDateMax = QLabel(self.frameSearch)
        self.labelDateMax.setObjectName(u"labelDateMax")

        self.formSearch.setWidget(4, QFormLayout.LabelRole, self.labelDateMax)

        self.timeDateMax = QDateTimeEdit(self.frameSearch)
        self.timeDateMax.setObjectName(u"timeDateMax")

        self.formSearch.setWidget(4, QFormLayout.FieldRole, self.timeDateMax)

        self.labelTitle = QLabel(self.frameSearch)
        self.labelTitle.setObjectName(u"labelTitle")

        self.formSearch.setWidget(0, QFormLayout.LabelRole, self.labelTitle)


        self.verticalLayout_2.addLayout(self.formSearch)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btnFormSearch = QPushButton(self.frameSearch)
        self.btnFormSearch.setObjectName(u"btnFormSearch")
        self.btnFormSearch.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_2.addWidget(self.btnFormSearch, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frameSearch)

        self.horizontalSpacer = QSpacerItem(327, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addWidget(self.frameSearchContainer)

        self.frameResultsContainer = QFrame(self.pageHome)
        self.frameResultsContainer.setObjectName(u"frameResultsContainer")
        self.frameResultsContainer.setCursor(QCursor(Qt.PointingHandCursor))
        self.frameResultsContainer.setFrameShape(QFrame.NoFrame)
        self.frameResultsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameResultsContainer)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frameResultsContainer)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabFlatView = QWidget()
        self.tabFlatView.setObjectName(u"tabFlatView")
        self.horizontalLayout_4 = QHBoxLayout(self.tabFlatView)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.resultsList = QListWidget(self.tabFlatView)
        QListWidgetItem(self.resultsList)
        self.resultsList.setObjectName(u"resultsList")
        self.resultsList.setFrameShape(QFrame.Box)

        self.horizontalLayout_4.addWidget(self.resultsList)

        self.tabWidget.addTab(self.tabFlatView, "")
        self.tabTreeView = QWidget()
        self.tabTreeView.setObjectName(u"tabTreeView")
        self.horizontalLayout_5 = QHBoxLayout(self.tabTreeView)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.resultsColumn = QColumnView(self.tabTreeView)
        self.resultsColumn.setObjectName(u"resultsColumn")
        self.resultsColumn.setFrameShape(QFrame.Box)

        self.horizontalLayout_5.addWidget(self.resultsColumn)

        self.tabWidget.addTab(self.tabTreeView, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.viewResults = QGraphicsView(self.frameResultsContainer)
        self.viewResults.setObjectName(u"viewResults")
        self.viewResults.setFrameShape(QFrame.Box)

        self.horizontalLayout_3.addWidget(self.viewResults)


        self.verticalLayout_6.addWidget(self.frameResultsContainer)

        self.widgetPages.addWidget(self.pageHome)
        self.pageDownload = QWidget()
        self.pageDownload.setObjectName(u"pageDownload")
        self.verticalLayout_8 = QVBoxLayout(self.pageDownload)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frameDownloadListContainer = QFrame(self.pageDownload)
        self.frameDownloadListContainer.setObjectName(u"frameDownloadListContainer")
        self.frameDownloadListContainer.setFrameShape(QFrame.NoFrame)
        self.frameDownloadListContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frameDownloadListContainer)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frameDownloadList = QFrame(self.frameDownloadListContainer)
        self.frameDownloadList.setObjectName(u"frameDownloadList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameDownloadList.sizePolicy().hasHeightForWidth())
        self.frameDownloadList.setSizePolicy(sizePolicy1)
        self.frameDownloadList.setMinimumSize(QSize(400, 0))
        self.frameDownloadList.setMaximumSize(QSize(400, 16777215))
        self.frameDownloadList.setFrameShape(QFrame.NoFrame)
        self.frameDownloadList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frameDownloadList)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.labelDownload = QLabel(self.frameDownloadList)
        self.labelDownload.setObjectName(u"labelDownload")
        self.labelDownload.setMargin(6)

        self.verticalLayout_7.addWidget(self.labelDownload)

        self.textEditDownloadEntries = QPlainTextEdit(self.frameDownloadList)
        self.textEditDownloadEntries.setObjectName(u"textEditDownloadEntries")
        self.textEditDownloadEntries.setFrameShape(QFrame.Box)

        self.verticalLayout_7.addWidget(self.textEditDownloadEntries)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.btnDownload = QPushButton(self.frameDownloadList)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setMaximumSize(QSize(70, 16777215))

        self.verticalLayout_7.addWidget(self.btnDownload, 0, Qt.AlignHCenter)


        self.horizontalLayout_9.addWidget(self.frameDownloadList)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.frameDownloadOptions = QFrame(self.frameDownloadListContainer)
        self.frameDownloadOptions.setObjectName(u"frameDownloadOptions")
        self.frameDownloadOptions.setMinimumSize(QSize(110, 0))
        self.frameDownloadOptions.setFrameShape(QFrame.NoFrame)
        self.frameDownloadOptions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frameDownloadOptions)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.btnLoadCSV = QPushButton(self.frameDownloadOptions)
        self.btnLoadCSV.setObjectName(u"btnLoadCSV")

        self.verticalLayout_10.addWidget(self.btnLoadCSV)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_6)

        self.btnLoadSaved = QPushButton(self.frameDownloadOptions)
        self.btnLoadSaved.setObjectName(u"btnLoadSaved")

        self.verticalLayout_10.addWidget(self.btnLoadSaved)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)


        self.horizontalLayout_9.addWidget(self.frameDownloadOptions)

        self.horizontalSpacer_2 = QSpacerItem(327, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addWidget(self.frameDownloadListContainer)

        self.frameDownloadContainer = QFrame(self.pageDownload)
        self.frameDownloadContainer.setObjectName(u"frameDownloadContainer")
        self.frameDownloadContainer.setCursor(QCursor(Qt.PointingHandCursor))
        self.frameDownloadContainer.setFrameShape(QFrame.NoFrame)
        self.frameDownloadContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frameDownloadContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frameDownloadContainer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMargin(6)

        self.verticalLayout_9.addWidget(self.label_3)

        self.viewDownloadedList = QTreeView(self.frameDownloadContainer)
        self.viewDownloadedList.setObjectName(u"viewDownloadedList")
        self.viewDownloadedList.setFrameShape(QFrame.Box)

        self.verticalLayout_9.addWidget(self.viewDownloadedList)


        self.verticalLayout_8.addWidget(self.frameDownloadContainer)

        self.widgetPages.addWidget(self.pageDownload)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.horizontalLayout_7 = QHBoxLayout(self.pageSettings)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.pageSettings)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.widgetPages.addWidget(self.pageSettings)
        self.pageAbout = QWidget()
        self.pageAbout.setObjectName(u"pageAbout")
        self.horizontalLayout_6 = QHBoxLayout(self.pageAbout)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelAbout = QLabel(self.pageAbout)
        self.labelAbout.setObjectName(u"labelAbout")

        self.horizontalLayout_6.addWidget(self.labelAbout)

        self.widgetPages.addWidget(self.pageAbout)

        self.verticalLayout_5.addWidget(self.widgetPages)


        self.horizontalLayout_2.addWidget(self.framePagesContainer)


        self.verticalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        self.widgetPages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Geddit", None))
        self.actionAuthentication.setText(QCoreApplication.translate("MainWindow", u"Authentication", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btnPageHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btnPageDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.btnPageSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btnPageAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.labelGeddit.setText(QCoreApplication.translate("MainWindow", u"Geddit v1.0", None))
        self.labelSubreddit.setText(QCoreApplication.translate("MainWindow", u"Subreddit", None))
        self.labelAuthor.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.labelDateMin.setText(QCoreApplication.translate("MainWindow", u"Date Min.", None))
        self.labelDateMax.setText(QCoreApplication.translate("MainWindow", u"Date Max", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.btnFormSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))

        __sortingEnabled = self.resultsList.isSortingEnabled()
        self.resultsList.setSortingEnabled(False)
        ___qlistwidgetitem = self.resultsList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        self.resultsList.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFlatView), QCoreApplication.translate("MainWindow", u"Flat View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTreeView), QCoreApplication.translate("MainWindow", u"Tree View", None))
        self.labelDownload.setText(QCoreApplication.translate("MainWindow", u"Download Sources (post/user/subreddit)", None))
        self.btnDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.btnLoadCSV.setText(QCoreApplication.translate("MainWindow", u"Load from CSV", None))
        self.btnLoadSaved.setText(QCoreApplication.translate("MainWindow", u"Load Saved Media", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.labelAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

