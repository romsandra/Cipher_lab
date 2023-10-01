import numpy as np
import random

# Задаём матрицы для кода Хэмминга(4,7) и алфавит
G = np.array([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
H = np.array([[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]])
R = np.array([[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]])
print('G^T =', G)
print('H =', H)
print('R =', R)
alp = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# Переводим сообщение в двоичный код
def message_to_bin(alphabet, message):
    str1 = [bin(alphabet.index(i))[2:] for i in message]
    str2 = ''
    for i in str1:
        for _ in range(10):
            if len(i) < 5:
                i = '0' + str(i)
        str2 += i
    return str2

# Делим массив на блоки. Необходимо для умножения на матрицу
def div_into_blocks(m, array):
    blocks = [array[i:i + m] for i in range(0, len(array), m)]
    return blocks

# Перемножение массива и блоков, полученных в предыдущей функции
def matrix_multiply(blocks, matrix, n):
    result = []
    for block in blocks:
        col = np.array([[int(digit)] for digit in block])
        cipher = (matrix @ col) % n
        result.extend(cipher.flatten() % n)
    return result

# В двоичном коде меняем 0 на 1 и наоборот для добавления и исправления ошибок
def add_error(a, b):
    if a[b] == 0:
        a[b] = 1
    else:
        a[b] = 0
    return a

# Достаём ключ по значению
def get_key(dict, value):
    for key, v in dict.items():
        if v == value:
            return key

# Расшифровываем получившийся результат, переводя двоичный код в сообщение
def encrypted(blox):
    result = matrix_multiply(blox, R, 2)
    # Разбиение на блоки
    digits = ''.join(str(i) for i in result)
    blocks = div_into_blocks(5, digits)
    print(blocks)
    # Преобразование цифр в буквы
    word = ''.join(get_key(dict, i) for i in blocks)
    return word

# Осуществляем проверку с матрицей H
def check_H(list, matrix_H):
    blox = div_into_blocks(7, list)
    check = matrix_multiply(blox, matrix_H, 2)
    print('Результат: ', check)
    blox = div_into_blocks(3, check)
    k = 1
    for block in blox:
        col = np.array([int(digit) for digit in block])
        # Определяем, какому столбцу матрицы H соответсвует код ошибки
        decimal_num = get_key(dict_H, ''.join(map(str, col)))
        if decimal_num != 0:
            add_error(list, decimal_num + (k - 1) * 7 - 1)
            digits = ''.join(str(i) for i in list)
            blox = div_into_blocks(7, digits)
            k += 1
    return list, blox


# Словарь для матрицы H
bins1 = [0, 1, 2, 3, 4, 5, 6, 7]
bins2 = ['000', '100', '010', '110', '001', '101', '011', '111']
dict_H = dict(zip(bins1, bins2))

# Создание словаря для перевода двоичных чисел в буквы
bins = message_to_bin(alp, alp)
bins = div_into_blocks(5, bins)
dict = dict(zip(alp, bins))


# Переводим каждую букву слова в двоичный код
print('Переводим каждую букву слова "гном" в двоичный код')
digits = message_to_bin(alp, 'гном')
# Разбиение на блоки
blocks = div_into_blocks(4, digits)
print(blocks)

# Умножение каждого блока на матрицу G
print('Умножение каждого блока на матрицу G')
result = matrix_multiply(blocks, G, 2)
# Сохраняем результат в другую переменную, чтобы повторно использовать
result_base = result
print(result, '\n')

# Вредоносное вмешательство
print('Вредоносное вмешательство\n')

print('Один испорченный бит')
# Меняем один бит
result = add_error(result, 5)
digits = ''.join(str(i) for i in result)
print(result)

# Проверка с матрицей H
print('Проверка с матрицей H')
result, blocks = check_H(result, H)
print(blocks)

print('Исправление ошибок:\n', result)
print('Дешифрование')
word = encrypted(blocks)
print(word, '\n')

# Меняем два бита
result = result_base
print('Два испорченных бита')
result = add_error(result, 5)
result = add_error(result, 12)
digits = ''.join(str(i) for i in result)
print(result)

# Проверка с матрицей H
print('Проверка с матрицей H')
result, blocks = check_H(result, H)

print('Исправление ошибок:\n', result)
print('Дешифрование')
word = encrypted(blocks)
print(word, '\n')

# Меняем три бита
result = result_base
print('Три испорченных бита')
result = add_error(result, 5)
result = add_error(result, 12)
result = add_error(result, 19)
digits = ''.join(str(i) for i in result)
print(result)

# Проверка с матрицей H
print('Проверка с матрицей H')
result, blocks = check_H(result, H)

print('Исправление ошибок:\n', result)
print('Дешифрование')
word = encrypted(blocks)
print(word, '\n')

# Меняем четыре бита
result = result_base
print('Четыре испорченных бита')
result = add_error(result, 5)
result = add_error(result, 12)
result = add_error(result, 19)
result = add_error(result, 26)
digits = ''.join(str(i) for i in result)
print(result)

# Проверка с матрицей H
print('Проверка с матрицей H')
result, blocks = check_H(result, H)

print('Исправление ошибок:\n', result)
print('Дешифрование')
word = encrypted(blocks)
print(word)
