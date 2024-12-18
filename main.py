from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox
from logic import SaperLogic

class SaperGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Saper")
        self.setGeometry(100, 100, 600, 600)
        self.rows = 8
        self.cols = 8
        self.bombs = 10
        self.logic = SaperLogic(self.rows, self.cols, self.bombs)
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget()
        self.layout = QGridLayout()
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                btn = QPushButton("")
                btn.setFixedSize(50, 50)
                btn.clicked.connect(lambda checked, r=row, c=col: self.on_click(r, c))
                self.layout.addWidget(btn, row, col)
                self.buttons[row][col] = btn

        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

    def on_click(self, row, col):
        if self.logic.board[row][col] == -1:
            self.game_over(False)
        else:
            self.logic.reveal(row, col)
            self.update_buttons()
            if self.check_win():
                self.game_over(True)

    def update_buttons(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.logic.revealed[row][col]:
                    value = self.logic.board[row][col]
                    self.buttons[row][col].setText("" if value == 0 else str(value))
                    self.buttons[row][col].setEnabled(False)

    def game_over(self, won):
        msg = QMessageBox()
        msg.setWindowTitle("Koniec Gry")
        if won:
            msg.setText("Wygra³eœ!")
        else:
            msg.setText("Przegra³eœ! Trafi³eœ na bombê.")
        msg.exec_()
        self.close()

    def check_win(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.logic.revealed[row][col] and self.logic.board[row][col] != -1:
                    return False
        return True


if __name__ == "__main__":
    app = QApplication([])
    window = SaperGame()
    window.show()
    app.exec_()

