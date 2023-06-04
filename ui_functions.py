from PyQt6.QtCore import (
    QPropertyAnimation,
    QEasingCurve
)

from gui import *

class UIFunctions(MainWindow):
    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frameSideMenu.width()
            maxExtend = maxWidth
            standard = 70

            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self.ui.frameSideMenu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()