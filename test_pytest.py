import pytest
from main import generate_number, validate_input, calculate_bulls_and_cows


def test_generate_number():
    """
    Проверка функции генерации числа:
    - длина числа,
    - уникальность цифр,
    - обработка исключений.
    """
    for length in range(1, 11):
        number = generate_number(length)
        assert len(number) == length, f"Длина числа должна быть {length}"
        assert len(set(number)) == length, ("Цифры в числе должны "
                                            "быть уникальны")

    with pytest.raises(ValueError):
        generate_number(0)  # Неверная длина
    with pytest.raises(ValueError):
        generate_number(11)  # Неверная длина


@pytest.mark.parametrize(
    "user_input, length, expected",
    [
        # Корректный ввод
        ("1234", 4, (True, "")),
        # Некорректная длина
        ("12", 4, (False, "Число должно быть длиной 4 символов.")),
        # Некорректные символы
        ("12a4", 4, (False, "Число должно содержать только цифры.")),
        # Повторяющиеся цифры
        ("1123", 4, (False, "Число должно содержать уникальные цифры.")),
    ],
)
def test_validate_input(user_input, length, expected):
    """
    Проверка функции валидации ввода пользователя.
    """
    result = validate_input(user_input, length)
    assert result == expected, (
        f"Для ввода {user_input} " f"ожидался результат {expected}"
    )


@pytest.mark.parametrize(
    "secret, guess, expected_bulls, expected_cows",
    [
        ("1234", "1243", 2, 2),  # Частичное совпадение
        ("1234", "5678", 0, 0),  # Полное несовпадение
        ("1234", "1234", 4, 0),  # Полное совпадение
        ("1234", "4321", 0, 4),  # Все цифры совпадают, но не на своих местах
    ],
)
def test_calculate_bulls_and_cows(secret, guess,
                                  expected_bulls, expected_cows):
    """
    Проверка функции подсчета быков и коров.
    """
    bulls, cows = calculate_bulls_and_cows(secret, guess)
    assert bulls == expected_bulls, (
        f"Ожидалось {expected_bulls} " f"быков для {secret} и {guess}"
    )
    assert cows == expected_cows, (
        f"Ожидалось {expected_cows} " f"коров для {secret} и {guess}"
    )
