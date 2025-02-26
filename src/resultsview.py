from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class ResultsView(QWidget):
    def __init__(self, score, play_again_callback):
        super().__init__()

        self.layout = QVBoxLayout(self)
        
        self.result_label = QLabel(self)
        self.result_label.setObjectName("resultLabel")  
        self.result_label.setAlignment(Qt.AlignCenter)  
        self.layout.addWidget(self.result_label)

        self.play_again_button = QPushButton("Zagraj jeszcze raz", self)
        self.play_again_button.setObjectName("playAgainButton")  
        self.play_again_button.clicked.connect(play_again_callback)
        self.layout.addWidget(self.play_again_button)

    def show_results(self, score, total_questions):
        self.result_label.setText(f"Twój wynik: {score} / {total_questions}")
