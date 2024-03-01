# Определение функции для фильтрации строк
def filter_strings(strings):
    return [s for s in strings if len(s) <= 3]

# Тестирование функции с предоставленными примерами
print(filter_strings(["Hello", "2", "world", ":-)"]))  # Ожидаемый результат: ["2", ":-)"]
print(filter_strings(["1234", "1567", "-2", "computer science"]))  # Ожидаемый результат: ["-2"]
print(filter_strings(["Russia", "Denmark", "Kazan"]))  # Ожидаемый результат: []
