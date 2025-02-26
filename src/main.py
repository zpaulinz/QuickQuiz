import sys
from PyQt5.QtWidgets import QApplication
from quickquiz import QuickQuiz

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuickQuiz()
    window.show()
    sys.exit(app.exec_())
