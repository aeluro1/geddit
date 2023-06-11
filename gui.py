import sys

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)

from ui_mainwindow import Ui_MainWindow
from ui_functions import UIFunctions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent = None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
    def _setupCallbacks(self):
        pass

    def _initializeSignalsAndSlots(self):
        self._view.ui.btnPageHome.clicked.connect(lambda: self._view.ui.widgetPages.setCurrentIndex(0))
        self._view.ui.btnPageDownload.clicked.connect(lambda: self._view.ui.widgetPages.setCurrentIndex(1))
        self._view.ui.btnPageSettings.clicked.connect(lambda: self._view.ui.widgetPages.setCurrentIndex(2))
        self._view.ui.btnPageAbout.clicked.connect(lambda: self._view.ui.widgetPages.setCurrentIndex(3))


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    controller = GedditController(model = None, view = mainWindow)
    mainWindow.show() # show window
    sys.exit(app.exec()) # initiate event loop

if __name__ == "__main__":
    main()