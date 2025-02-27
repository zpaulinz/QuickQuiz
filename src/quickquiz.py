import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QButtonGroup, QStackedWidget
from questionview import QuestionView
from resultsview import ResultsView

class QuickQuiz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickQuiz")
        self.setFixedSize(500, 300)

        # Load CSS styles
        self.load_styles()
        
        # Load questions from a JSON file
        with open('questions.json', 'r', encoding='utf-8') as f:
            self.questions = json.load(f)

        self.current_question = 0
        self.score = 0

        # Stacked widget to switch between different views
        self.stacked_widget = QStackedWidget(self)
        self.layout = QVBoxLayout(self)

        # Create question and results views
        self.create_question_view()
        self.create_results_view()

        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)

    def create_question_view(self):
        # Initialize the question view and add it to the stacked widget
        self.question_view = QuestionView(self.questions[self.current_question], self.check_answer)
        self.stacked_widget.addWidget(self.question_view)

    def create_results_view(self):
        # Initialize the results view and add it to the stacked widget
        self.results_view = ResultsView(self.score, self.play_again)
        self.stacked_widget.addWidget(self.results_view)

    def check_answer(self, selected_answer):
        # Check if the selected answer is correct
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if selected_answer.lower() == correct_answer.lower():
            self.score += 1

        # Move to the next question
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_results()

    def update_question(self):
        # Update the displayed question
        self.question_view.update(self.questions[self.current_question])

    def show_results(self):
        # Update the results view with the final score
        self.results_view.show_results(self.score, len(self.questions))
        # Switch to the results view
        self.stacked_widget.setCurrentWidget(self.results_view)

    def play_again(self):
        # Reset the quiz
        self.current_question = 0
        self.score = 0
        self.update_question()
        self.stacked_widget.setCurrentWidget(self.question_view)
        
    def load_styles(self):
        # Load CSS styles from a file
        try:
            with open('style.css', 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print("Plik style.css nie został znaleziony.")
