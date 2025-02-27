from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup, QPushButton
from PyQt5.QtCore import Qt

class QuestionView(QWidget):
    def __init__(self, question_data, check_answer_callback):
        super().__init__()
        self.question_data = question_data
        self.check_answer_callback = check_answer_callback

        # Create a vertical layout for the question view
        question_layout = QVBoxLayout(self)

        # Create and center the question label
        self.question_label = QLabel(self.question_data["question"], self)
        self.question_label.setAlignment(Qt.AlignCenter)  
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

    def update(self, question_data):
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
