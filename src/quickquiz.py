import json
import random
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget
from startview import StartView
from questionview import QuestionView
from resultsview import ResultsView

class QuickQuiz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickQuiz")
        self.setFixedSize(500, 300)

        # Load CSS styles
        self.load_styles()
        
        # Load questions
        with open('questions.json', 'r', encoding='utf-8') as f:
            self.questions = json.load(f)
        random.shuffle(self.questions)

        self.current_question = 0
        self.score = 0

        # Stacked widget to switch between views
        self.stacked_widget = QStackedWidget(self)
        self.layout = QVBoxLayout(self)

        # Create views
        self.create_start_view()
        self.create_question_view()
        self.create_results_view()

        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)
        
        
    # Initialize the start view
    def create_start_view(self):   
        self.start_view = StartView(self.start_quiz)
        self.stacked_widget.addWidget(self.start_view)


    # Initialize the question view
    def create_question_view(self):
        self.question_view = QuestionView(self.questions[self.current_question], self.check_answer)
        self.stacked_widget.addWidget(self.question_view)
        
        
    # Initialize the results view
    def create_results_view(self):
        self.results_view = ResultsView(self.score, self.play_again)
        self.stacked_widget.addWidget(self.results_view)


    # Check the selected answer and update score
    def check_answer(self, selected_answer):
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if selected_answer.lower() == correct_answer.lower():
            self.score += 1

        self.question_view.color_answers()

        # Move to the next question or show results
        self.current_question += 1
        if self.current_question < len(self.questions):
            QTimer.singleShot(1200, self.question_view.reset_answers)  
            QTimer.singleShot(1200, self.update_question)          
        else:
            # Last question
            self.update_progress_bar(100)  
        
            # Set a timer to delay showing results
            QTimer.singleShot(1500, self.show_results)  # 1200 ms = 1.2 s
    
    
    # Update the progress bar value 
    def update_progress_bar(self, progress):
        self.question_view.progress_bar.setValue(progress)
            
            
    # Update question and progress
    def update_question(self):
        # Calculate the progress
        progress = int(((self.current_question + 0) / len(self.questions)) * 100)
        
        is_last_question = self.current_question == len(self.questions) -1
        # Update the displayed question
        question_data = self.questions[self.current_question].copy()
        random.shuffle(question_data["options"])
        
        self.question_view.update(question_data, progress, is_last_question)


    # Show the results after quiz ends
    def show_results(self):
        # Update the results view with the final score
        self.results_view.show_results(self.score, len(self.questions))
        
        # Switch to the results view
        self.stacked_widget.setCurrentWidget(self.results_view)


    # Restart the quiz
    def play_again(self):
        self.current_question = 0
        self.score = 0
        
        self.question_view.reset_answers()
        self.question_view.reset_button()
        random.shuffle(self.questions)
        
        self.update_question()
        self.stacked_widget.setCurrentWidget(self.start_view)
    
    # Start the quiz
    def start_quiz(self):
        self.stacked_widget.setCurrentWidget(self.question_view)
        
        
    # Load CSS styles from a file   
    def load_styles(self):    
        try:
            with open('style.css', 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print("Plik style.css nie został znaleziony.")
