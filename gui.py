import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QWidget, QSpinBox, QMessageBox
)
from main import generate_number, validate_input, calculate_bulls_and_cows


class BullsAndCowsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Быки и Коровы")
        self.setGeometry(100, 100, 400, 300)

        self.secret_number = ""
        self.length = 4  # Длина числа по умолчанию
        self.attempts = []  # История попыток

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Выбор длины числа
        self.length_label = QLabel("Выберите длину числа (2–7):")
        layout.addWidget(self.length_label)

        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(2, 7)
        self.length_spinbox.setValue(4)
        layout.addWidget(self.length_spinbox)

        # Кнопка для старта игры
        self.start_button = QPushButton("Начать игру")
        self.start_button.clicked.connect(self.start_game)
        layout.addWidget(self.start_button)

        # Поле для ввода числа
        self.input_label = QLabel("Введите ваше число:")
        self.input_label.hide()
        layout.addWidget(self.input_label)

        self.input_field = QLineEdit()
        self.input_field.hide()
        layout.addWidget(self.input_field)

        # Кнопка для проверки числа
        self.submit_button = QPushButton("Отправить")
        self.submit_button.clicked.connect(self.check_guess)
        self.submit_button.hide()
        layout.addWidget(self.submit_button)

        # История попыток
        self.history_label = QLabel("История попыток:")
        self.history_label.hide()
        layout.addWidget(self.history_label)

        self.history_field = QLabel("")
        self.history_field.hide()
        layout.addWidget(self.history_field)

        # Контейнер
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_game(self):
        self.length = self.length_spinbox.value()
        self.secret_number = generate_number(self.length)
        self.attempts = []

        self.input_label.show()
        self.input_field.show()
        self.submit_button.show()
        self.history_label.show()
        self.history_field.show()

        self.length_label.hide()
        self.length_spinbox.hide()
        self.start_button.hide()

        # только для тестов, иначе долго отгадывать
        print(f"Секретное число (для отладки): {self.secret_number}")

    def check_guess(self):
        user_input = self.input_field.text()
        is_valid, error_message = validate_input(user_input, self.length)

        if not is_valid:
            QMessageBox.warning(self, "Ошибка", error_message)
            return

        bulls, cows = calculate_bulls_and_cows(self.secret_number, user_input)
        self.attempts.append(f"Число: {user_input},"
                             f"Быки: {bulls}, Коровы: {cows}")
        self.history_field.setText("\n".join(self.attempts))

        if bulls == self.length:
            QMessageBox.information(self, "Победа!",
                                    f"Вы угадали число {self.secret_number}!")
            self.reset_game()

    def reset_game(self):
        self.secret_number = ""
        self.length = 4
        self.attempts = []

        self.input_label.hide()
        self.input_field.hide()
        self.submit_button.hide()
        self.history_label.hide()
        self.history_field.hide()

        self.length_label.show()
        self.length_spinbox.show()
        self.start_button.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BullsAndCowsApp()
    window.show()
    sys.exit(app.exec())
