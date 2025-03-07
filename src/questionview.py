from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup, QPushButton, QProgressBar, QStyleOptionProgressBar
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor

class QuestionView(QWidget):
    def __init__(self, question_data, check_answer_callback):
        super().__init__()
        self.question_data = question_data
        self.check_answer_callback = check_answer_callback
        
        # Create a vertical layout for the question view
        question_layout = QVBoxLayout(self)

        # Create progress bar
        self.progress_bar = CustomProgressBar(self)
        self.progress_bar.setRange(0,100)
        self.progress_bar.setFixedHeight(10)
        self.progress_bar.setTextVisible(False)
        question_layout.addWidget(self.progress_bar)

        # Create and center the question label
        self.question_label = QLabel(self.question_data["question"], self)
        self.question_label.setAlignment(Qt.AlignCenter)  
        self.question_label.setWordWrap(True)
        question_layout.addWidget(self.question_label)

        # Layout for radio buttons (answer options)
        self.radio_buttons_layout = QVBoxLayout()
        self.button_group = QButtonGroup(self)
        self.radio_buttons = []

        # Create radio buttons for answer options
        for i, option in enumerate(self.question_data["options"]):
            radio_button = QRadioButton(option, self)
            self.radio_buttons_layout.setAlignment(Qt.AlignCenter)
            self.radio_buttons_layout.addWidget(radio_button)
            self.button_group.addButton(radio_button, i)
            self.radio_buttons.append(radio_button)

        question_layout.addLayout(self.radio_buttons_layout)

        # Create submit button
        self.submit_button = QPushButton("Sprawdź odpowiedź", self)
        self.submit_button.clicked.connect(self.submit_answer)
        question_layout.addWidget(self.submit_button)
        

    def submit_answer(self):
        """Submit the answer and call the callback."""
        selected_button = self.button_group.checkedButton()
        if selected_button:
            self.check_answer_callback(selected_button.text())
            self.color_answers()
            
            # Disable the buttons to prevent further changes
            for radio_button in self.radio_buttons:
                radio_button.setEnabled(False)


    def color_answers(self):
        correct_answer = self.question_data["correct_answer"]
        
        for radio_button in self.radio_buttons:
            if radio_button.text().lower() == correct_answer.lower():
                radio_button.setStyleSheet("color: green; font-weight: bold;")
            else:
                radio_button.setStyleSheet("color: red; ")


    def reset_answers(self):
        """Reset the colors and enable the radio buttons."""
        for radio_button in self.radio_buttons:
            radio_button.setStyleSheet("")  
            radio_button.setEnabled(True)
            
        # Reset any selections
        self.button_group.setExclusive(False)
        for radio_button in self.radio_buttons:
            radio_button.setChecked(False)
        self.button_group.setExclusive(True)


    def update(self, question_data, progress, is_last_question=False):
        """Update the question view with new question data."""
        self.question_data = question_data
        self.question_label.setText(self.question_data["question"])

        # Update answer options
        for i, option in enumerate(self.question_data["options"]):
            self.radio_buttons[i].setText(option)

        # Reset radio button selection
        self.button_group.setExclusive(False)
        for radio_button in self.radio_buttons:
            radio_button.setChecked(False)
        self.button_group.setExclusive(True)
        
        #Update the progress bar
        self.progress_bar.setValue(progress)
        
        # If it's the last question, update the submit button
        if is_last_question:
            self.set_last_question()
        else:
            self.reset_button()
            

    def set_last_question(self):
        self.submit_button.setText("Podsumowanie")
        self.submit_button.setStyleSheet("background-color: #FF00C3;")
        
        
    def reset_button(self):
        self.submit_button.setText("Sprawdź odpowiedź")
        self.submit_button.setStyleSheet("")


class CustomProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
    

    def paintEvent(self, event):
        # Utworzenie obiektu QStyleOptionProgressBar, by uzyskać informacje o postępie
        option = QStyleOptionProgressBar()
        self.initStyleOption(option)

        # Tworzymy obiekt QPainter do rysowania
        painter = QPainter(self)

        # Włączamy wygładzanie
        painter.setRenderHint(QPainter.Antialiasing)

        # Malowanie tła progress bar'a
        painter.setBrush(QColor("#f0f0f0"))  # Kolor tła (jasny szary)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(option.rect, 5, 5)  # Rysowanie zaokrąglonego tła

        # Obliczanie szerokości wypełnienia progress bar'a
        fill_rect = QRect(option.rect)
        fill_rect.setWidth(int(option.rect.width() * self.value() / 100))  # Dopasowanie szerokości wypełnienia na podstawie wartości

        # Malowanie wypełnienia progress bar'a
        if self.value() < 100:
            painter.setBrush(QColor("#0059ff"))  # Kolor niebieski, jeśli postęp < 100%
        else:
            painter.setBrush(QColor("#FF00C3"))  # Kolor różowy, jeśli postęp == 100%
        painter.drawRoundedRect(fill_rect, 5, 5)  # Rysowanie wypełnionego obszaru (zaokrąglone rogi)

        # Kończymy malowanie
        painter.end()
