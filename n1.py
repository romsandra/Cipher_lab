# Задание 1
import numpy as np

alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,?! '
key_list = list([_ for _ in alp])
n = len(key_list)
value_list = list([_ for _ in range(0, n)])
dict = dict(zip(key_list, value_list))

message = 'я люблю тебя'
print('Изначальное сообщение: ', message)

m1 = np.array([[4, 5], [3, 4]])
m2 = np.array([[2, 3, 1], [3, 4, 1], [2, 3, 2]])
m3 = np.array([[1, 2, 3, 4], [2, 3, 1, 2], [1, 1, 1, -1], [1, 0, -2, -6]])

# Разбиение строки на блоки
def div_into_blocks(m, list):
    blocks = [list[i:i + m] for i in range(0, len(list), m)]
    return blocks

# Преобразование строки в столбец и перемножение с матрицей
# Выводит строку, содержащую в себе все результаты перемножения
def matrix_multiply(blocks, matrix, n):
    result = []
    for block in blocks:
        col = np.array([[int(digit)] for digit in block])
        cipher = (matrix @ col) % n
        result.extend(cipher.flatten() % n)
    return result

# Достаём ключ по значению
def get_key(dict, value):
    for key, v in dict.items():
        if v == value:
            return key

digits = [alp.index(i) for i in message]
print(digits)
print('Умножение на матрицу 2*2')
# Разбиение строки на блоки
blocks = div_into_blocks(2, digits)
# Умножение каждого блока на ключевую матрицу
result1 = matrix_multiply(blocks, m1, n)
# Преобразование цифр в буквы
cipher_text1 = "".join([alp[digit] for digit in result1])
#[alp.index(i) for i in result]
print(cipher_text1)

print('Умножение на матрицу 3*3')
# Разбиение строки на блоки
blocks = div_into_blocks(3, digits)
result2 = matrix_multiply(blocks, m2, n)
# Преобразование цифр в буквы
cipher_text2 = "".join([alp[digit] for digit in result2])
print(cipher_text2)

print('Умножение на матрицу 4*4')
# Разбиение строки на блоки
blocks = div_into_blocks(4, digits)
# Умножение каждого блока на ключевую матрицу
result3 = matrix_multiply(blocks, m3, n)
# Преобразование цифр в буквы
cipher_text3 = "".join([alp[digit] for digit in result3])
print(cipher_text3)

# Вредоносное вмешательство
print('Вредоносное вмешательство')
import random
cipher_text1 = cipher_text1.replace(list(cipher_text1)[0], random.choice(str(alp)))
cipher_text1 = cipher_text1.replace(list(cipher_text1)[1], random.choice(str(alp)))
cipher_text1 = cipher_text1.replace(list(cipher_text1)[2], random.choice(str(alp)))
cipher_text2 = cipher_text2.replace(list(cipher_text2)[0], random.choice(str(alp)))
cipher_text2 = cipher_text2.replace(list(cipher_text2)[1], random.choice(str(alp)))
cipher_text2 = cipher_text2.replace(list(cipher_text2)[2], random.choice(str(alp)))
cipher_text3 = cipher_text3.replace(list(cipher_text3)[0], random.choice(str(alp)))
cipher_text3 = cipher_text3.replace(list(cipher_text3)[1], random.choice(str(alp)))
cipher_text3 = cipher_text3.replace(list(cipher_text3)[2], random.choice(str(alp)))
print(cipher_text1)
print(cipher_text2)
print(cipher_text3)

# Расшифровка
print('Декодирование сообщений')
key_inv = np.linalg.inv(m1)
digits = [alp.index(letter) for letter in cipher_text1]
blocks = div_into_blocks(2, digits)
result1 = matrix_multiply(blocks, key_inv, n)
plain_text = "".join([(alp[int(round(digit) % n)]) for digit in result1])

print(plain_text)

key_inv = np.linalg.inv(m2)
digits = [alp.index(letter) for letter in cipher_text2]
blocks = div_into_blocks(3, digits)
result2 = matrix_multiply(blocks, key_inv, n)

plain_text = "".join([(alp[int(round(digit) % n)]) for digit in result2])

print(plain_text)

key_inv = np.linalg.inv(m3)
digits = [alp.index(letter) for letter in cipher_text3]
blocks = div_into_blocks(4, digits)
result3 = matrix_multiply(blocks, key_inv, n)
plain_text = "".join([(alp[int(round(digit) % n)]) for digit in result3])

print(plain_text)