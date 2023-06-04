import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,

    QWidget,

    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QGridLayout,

    QLabel,
    QLineEdit,
    QPushButton,
    QDialogButtonBox,

    QStatusBar,
    QToolBar
)

from ui_mainwindow import Ui_MainWindow
from ui_functions import UIFunctions

WINDOW_SIZE = (250, 300)

# Consider: Qt Designer, uic, pyuic6

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent = None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.setWindowTitle("Geddit")
        # self.setFixedSize(*WINDOW_SIZE)

        # self._generalLayout = QVBoxLayout()
        # centralWidget = QWidget(self)
        # centralWidget.setLayout(self._generalLayout)
        # self.setCentralWidget(centralWidget)

        # self._createMenu()
        # self._createToolbar()
        # self._createStatusBar()
        
        # self.buttons = []
        # self.buttons.append(QPushButton("temp"))

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolbar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)
    
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Initialized window")
        self.setStatusBar(status)

    def _createDisplay(self):
        self._display = QLineEdit()
        self._display.setFixedHeight(50)
        self._display.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._display.setReadOnly(True)
        self._generalLayout.addWidget(self._display)

    def setDisplayText(self, text):
        self._display.setText(text)
        self._display.setFocus()

    def getDisplayText(self):
        return self._display.text()
    
    def clearDisplayText(self):
        self.setDisplayText("")


        # layout = QVBoxLayout()
        # layout.addWidget(QPushButton("Download"))
        # test = QHBoxLayout()
        # test.addWidget(QPushButton("a"))
        # test.addWidget(QPushButton("a"))
        # test.addWidget(QPushButton("a"))
        # layout.addLayout(test)
        # layout.addWidget(QPushButton("test"))
        # self.setGeometry(100, 100, 280, 80)
        # self.setLayout(layout)

class GedditModel():
    def download(self, url):
        try:
            # Download code
            result = 0
        except Exception as e:
            result = 1
        return result
    
class GedditController():
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._functions = UIFunctions()
        self._initializeSignalsAndSlots()
    
    # Event handlers here
    def _callback(self):
        pass

    def _initializeSignalsAndSlots(self):
        self._view.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        # self._view.buttons[0].clicked.connect(partial(self._callback, 1))

        self._view.ui.btnPageHome.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self._view.ui.pageHome))
        self._view.ui.btnPageDownload.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self._view.ui.pageDownload))
        self._view.ui.btnPageSettings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self._view.ui.pageSettings))


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    controller = GedditController(model = None, view = mainWindow)
    mainWindow.show() # show window
    sys.exit(app.exec()) # initiate event loop

if __name__ == "__main__":
    main()