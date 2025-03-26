# Copyright (c) 2025 Paulina Zabielska

# All rights reserved. 
# This software may not be used, copied, modified, or distributed for commercial purposes without the prior written consent of the author.

from PyQt5.QtWidgets import QProgressBar, QStyleOptionProgressBar
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRect

class CustomProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    
    # Paint event for custom progress bar design
    def paintEvent(self, event):
        option = QStyleOptionProgressBar()
        self.initStyleOption(option)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Paint background of the progress bar
        painter.setBrush(QColor("#f0f0f0"))  
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(option.rect, 5, 5) 

        # Calculate and paint the fill width
        fill_rect = QRect(option.rect)
        fill_rect.setWidth(int(option.rect.width() * self.value() / 100))  

        # Paint the progress bar fill
        if self.value() < 100:
            painter.setBrush(QColor("#0059ff"))  
        else:
            painter.setBrush(QColor("#FF00C3"))  
        painter.drawRoundedRect(fill_rect, 5, 5)  

        painter.end()