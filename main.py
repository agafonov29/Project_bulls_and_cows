import random
from typing import Tuple


def generate_number(length: int) -> str:
    """
    Генерирует случайное число заданной длины с уникальными цифрами.

    Args:
        length (int): Длина числа (от 1 до 10).

    Returns:
        str: Случайное число длиной `length` с уникальными цифрами.

    Raises:
        ValueError: Если длина числа меньше 1 или больше 10.
    """
    if length < 1 or length > 10:
        raise ValueError("Длина числа должна быть от 1 до 10.")
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:length])


def validate_input(user_input: str, length: int) -> Tuple[bool, str]:
    """
    Проверяет, что ввод пользователя корректен:
    - Длина соответствует заданной.
    - Ввод состоит только из цифр.
    - Все цифры уникальны.

    Args:
        user_input (str): Ввод пользователя.
        length (int): Ожидаемая длина числа.

    Returns:
        Tuple[bool, str]:
            - Первый элемент: результат проверки (True/False).
            - Второй элемент: сообщение об ошибке или пустая
            строка при успешной проверке.
    """
    if len(user_input) != length:
        return False, f"Число должно быть длиной {length} символов."
    if not user_input.isdigit():
        return False, "Число должно содержать только цифры."
    if len(set(user_input)) != length:
        return False, "Число должно содержать уникальные цифры."
    return True, ""


def calculate_bulls_and_cows(secret: str, guess: str) -> Tuple[int, int]:
    """
    Считает количество "быков" и "коров" на основе секретного числа
    и попытки пользователя.

    Args:
        secret (str): Секретное число.
        guess (str): Попытка пользователя.

    Returns:
        Tuple[int, int]:
            - Количество "быков" (точное совпадение позиции и значения).
            - Количество "коров" (значение совпадает, но позиция нет).
    """
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows


if __name__ == "__main__":
    length = 4
    secret_number = generate_number(length)
    print(f"Секретное число (для отладки): {secret_number}")

    while True:
        user_input = input("Введите ваше число: ")
        is_valid, error_message = validate_input(user_input, length)
        if not is_valid:
            print(error_message)
            continue

        bulls, cows = calculate_bulls_and_cows(secret_number, user_input)
        print(f"Быки: {bulls}, Коровы: {cows}")

        if bulls == length:
            print("Поздравляю! Вы угадали число!")
            break
