# Copyright (c) 2025 Paulina Zabielska

# All rights reserved. 
# This software may not be used, copied, modified, or distributed for commercial purposes without the prior written consent of the author.

import sys
from PyQt5.QtWidgets import QApplication
from quickquiz import QuickQuiz

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion") 
    window = QuickQuiz()
    window.show()
    sys.exit(app.exec_())
