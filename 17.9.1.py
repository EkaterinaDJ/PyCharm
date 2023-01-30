#Напишите программу, которой на вход подается последовательность чисел через пробел,
#а также запрашивается у пользователя любое число.

array = '3 6 2 8 1 5 10 23 18 13 55 38'
lst = [int(i) for i in array.split()]
num = int(input('Enter a number from 0 to 55: '))

try:
    if 0 < num < 55:
        lst.append(num)
    else:
        num = int(input('Enter a valid number: '))
        lst.append(num)
except ValueError:
    print('Incorrect data')


#Сортировка списка по возрастанию элементов в нем (Сортировка пузырьком — самый любимый студентами вид сортировки)

for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)

#Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
#а следующий за ним больше или равен этому числу.

def bi_search(num: int, lst: list, left, right):
    len(lst)
    while left < right:
        middle = (left + right) // 2
        if lst[middle] < num:
            left = middle + 1
        else:
            right = middle
    return left
print('Element number:', bi_search(num, lst, 0, len(lst) - 1))