def filter_short_strings(strings):
    """
    Функция фильтрует строки из массива strings, оставляя только те, длина которых меньше или равна 3 символам.
    """
    result = []
    for s in strings:
        if len(s) <= 3:
            result.append(s)
    return result

# Пример использования
input_strings = ["Hello", "2", "world", ":-)"]
filtered_strings = filter_short_strings(input_strings)
print(filtered_strings)  # Выведет: ["2", ":-)"]
