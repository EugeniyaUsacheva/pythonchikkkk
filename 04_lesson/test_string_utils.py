import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тесты для метода capitalize

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),  # обычная строка
    ("hello world", "Hello world"),  # строка с пробелами
    ("python", "Python"),  # обычная строка
    ("Тест", "Тест"),  # строка с кириллицей
    ("123", "123"),  # строка с цифрами
    ("04 апреля 2023", "04 апреля 2023"),  # строка с пробелами
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    "",  # пустая строка
    " ",  # строка с пробелом
    None,  # None как вход
])
def test_capitalize_negative(input_str):
    if input_str is None:
        with pytest.raises(TypeError):  # ожидаем ошибку TypeError
            string_utils.capitalize(input_str)
    else:
        assert string_utils.capitalize(input_str) == input_str

# Тесты для метода trim

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),  # строка с пробелами в начале
    ("   hello", "hello"),  # строка с пробелами в начале
    ("   python  ", "python  "),  # строка с пробелами в начале и конце
    ("Тест", "Тест"),  # строка без пробелов
    ("04 апреля 2023", "04 апреля 2023"),  # строка с пробелами
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    "",  # пустая строка
    " ",  # строка с одним пробелом
    None,  # None как вход
])
def test_trim_negative(input_str):
    if input_str is None:
        with pytest.raises(TypeError):  # ожидаем ошибку TypeError
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == input_str

# Тесты для метода contains

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),  # символ присутствует в начале
    ("Hello World", "o", True),  # символ присутствует
    ("Python", "P", True),  # символ присутствует в начале
    ("Тест", "Т", True),  # кириллица
    ("123", "1", True),  # цифры
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),  # символ отсутствует
    ("Hello World", "z", False),  # символ отсутствует
    ("Python", "x", False),  # символ отсутствует
    ("", "S", False),  # пустая строка
    (" ", "S", False),  # строка с пробелом
    (None, "S", False),  # None как вход для строки
    ("SkyPro", None, False),  # None как вход для символа
])
def test_contains_negative(input_str, symbol, expected):
    if input_str is None or symbol is None:
        with pytest.raises(TypeError):  # ожидаем ошибку TypeError
            string_utils.contains(input_str, symbol)
    else:
        assert string_utils.contains(input_str, symbol) == expected

# Тесты для метода delete_symbol

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),  # удаление символа
    ("Hello World", "o", "Hell Wrld"),  # удаление символа
    ("Python", "P", "ython"),  # удаление первого символа
    ("Тест", "Т", "ест"),  # удаление кириллического символа
    ("123", "1", "23"),  # удаление цифры
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "Z", "SkyPro"),  # символ не найден
    ("Hello World", "x", "Hello World"),  # символ не найден
    ("Python", "p", "Python"),  # символ с маленькой буквы, игнорируется
    ("", "S", ""),  # пустая строка
    (" ", "S", " "),  # строка с одним пробелом
    (None, "S", None),  # None как вход
])
def test_delete_symbol_negative(input_str, symbol, expected):
    if input_str is None:
        with pytest.raises(TypeError):  # ожидаем ошибку TypeError
            string_utils.delete_symbol(input_str, symbol)
    else:
        assert string_utils.delete_symbol(input_str, symbol) == expected