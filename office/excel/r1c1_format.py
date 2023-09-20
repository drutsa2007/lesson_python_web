# Импорт необходимых методов из openpyxl.utils
from openpyxl.utils import get_column_letter, column_index_from_string

# Вывод 'A'
a = get_column_letter(1)
# Вывод '1'
b = column_index_from_string('A')
print(a, b)
