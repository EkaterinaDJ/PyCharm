numbers = input('Введите числа через пробел: ')
user_number = int(input('Введите любое число: '))

# Функция для определения цифр в строке
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

# Проверка соответствия указанному в условии ввода данных.

if " " not in numbers:
    print("\n Введите числа, согласно условию ввода (пробел).")
    numbers = input('Введите целые числа через пробел: ')
if not is_int(numbers):
    print('\n Введите числа, согласно условию ввода(числа).\n')
else:
    numbers = numbers.split()

# Меняем список строк на список чисел

list_numbers = [int(item) for item in numbers]


#Сортировка пузырьком

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(f'Упорядоченный по возрастанию список: {numbers})')

# Установка позиции элемента

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за пределы допустимого диапазона, введите меньшее число.'

if not binary_search(list_numbers, user_number, 0, len(list_numbers)):
    rI = min(list_numbers, key=lambda x: (abs(x - user_number), x))
    ind = list_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_number:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_numbers[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_numbers.index(rI)}
В списке нет меньшего элемента''')
    elif rI > user_number:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_numbers.index(rI)}
Ближайший меньший элемент: {list_numbers[min_ind]} его индекс: {min_ind}''')
    elif list_numbers.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_numbers.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_numbers, user_number, 0, len(list_numbers))}')