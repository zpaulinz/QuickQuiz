from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class ResultsView(QWidget):
    def __init__(self, score, play_again_callback):
        super().__init__()
        
        # Main layout for the results view
        self.layout = QVBoxLayout(self)
        
        # Result label setup to display the score
        self.result_label = QLabel(self)
        self.result_label.setObjectName("resultLabel")  
        self.result_label.setAlignment(Qt.AlignCenter)  
        self.layout.addWidget(self.result_label)
        
        # Description label setup to display the additional information
        self.description_label = QLabel(self)
        self.description_label.setObjectName("descriptionLabel")  
        self.description_label.setAlignment(Qt.AlignCenter)  
        self.description_label.setWordWrap(True)
        self.layout.addWidget(self.description_label)

        # Play again button setup
        self.play_again_button = QPushButton("Zagraj jeszcze raz", self)
        self.play_again_button.setObjectName("playAgainButton")  
        self.play_again_button.clicked.connect(play_again_callback)
        self.layout.addWidget(self.play_again_button)


    # Update and display the final score and additional information
    def show_results(self, score, total_questions):
        self.result_label.setText(f"Twój wynik: {score} / {total_questions}")
        
        percent_score = round(score / total_questions * 100)
        if score == total_questions:
            self.description_label.setText(f"Gratulacje! Znasz wszystkie odpowiedzi!")
        else:
            self.description_label.setText(f"Uzyskano {percent_score}% poprawnych odpowiedzi")
        
