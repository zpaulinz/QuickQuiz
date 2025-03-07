from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class StartView(QWidget):
    def __init__(self, start_game_callback):
        super().__init__()

        self.layout = QVBoxLayout(self)
    
        self.title_label = QLabel(self)
        self.title_label.setObjectName("titleLabel")  
        self.title_label.setAlignment(Qt.AlignBottom) 
        self.title_label.setText(f"QuickQuiz") 
        
        self.title_label.setFixedHeight(120)
        self.layout.addWidget(self.title_label)

        self.header_label = QLabel(self)
        self.header_label.setObjectName("headerLabel")  
        self.header_label.setAlignment(Qt.AlignTop)  
        self.header_label.setText(f"Sprawdź swoją wiedzę!") 

        self.header_label.setFixedHeight(120)
        self.layout.addWidget(self.header_label)
        
        self.start_button = QPushButton("Rozpocznij quiz", self)
        self.start_button.setObjectName("startButton")  
        self.start_button.clicked.connect(start_game_callback)
        self.header_label.setFixedHeight(200)
        self.layout.addWidget(self.start_button)
