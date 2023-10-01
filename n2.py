import numpy as np
import random

message1 = 'ты перегудин'
message2 = 'кто я что ли'
alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,?! '
n = len(alp)
matrix = np.array([[4, 5], [3, 4]])

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

def find_matrix_key(array1, array2, i, n):
    for a in range(n):
        for b in range(n):
            if (array1[0] * a + array1[1] * b) % n == array2[i]:
                if (array1[2] * a + array1[3] * b) % n == array2[i+2]:
                    if (array1[4] * a + array1[5] * b) % n == array2[i+4]:
                        if (array1[6] * a + array1[7] * b) % n == array2[i+6]:
                            if (array1[8] * a + array1[9] * b) % n == array2[i+8]:
                                if (array1[10] * a + array1[11] * b) % n == array2[i+10]:
                                    return a, b


# Зашифровываем наши сообщения
print('Изначальное сообщение 1: ', message1)
digits1 = [alp.index(i) for i in message1]
print(digits1)
blocks = div_into_blocks(len(matrix), digits1)
result1 = matrix_multiply(blocks, matrix, n)
print('Зашифрованное сообщение 1: ', result1)
cipher_text1 = "".join([alp[digit] for digit in result1])
print(cipher_text1)

print('Изначальное сообщение 2: ', message2)
digits2 = [alp.index(i) for i in message2]
print(digits2)
blocks = div_into_blocks(len(matrix), digits2)
result2 = matrix_multiply(blocks, matrix, n)
print('Зашифрованное сообщение 2: ', result2)
cipher_text2 = "".join([alp[digit] for digit in result2])
print(cipher_text2)

# Теперь делаем вид, что не знаем ключевую матрицу и одно(первое) первоначальное сообщение
print('Начнём дешифровку первого сообщения, зная только его кодированную версию, \n'
      'а также сообщение два и его закодированную версию')

P1 = [alp.index(letter) for letter in message1]
print('P1 =', P1)
C1 = [alp.index(letter) for letter in cipher_text1]
print('С1 =', C1)
print('K = C * P^(-1)')

# Находим ключевую матрицу
print('Находим ключевую матрицу')
col1 = find_matrix_key(P1, C1, 0, 38)
col2 = find_matrix_key(P1, C1, 1, 38)

K = np.concatenate(([col1], [col2]))
print('K =', K)

K = np.linalg.inv(K)
print('K^(-1) =', K)
C2 = [alp.index(letter) for letter in cipher_text2]
print('С2 =', C2)
blocks = div_into_blocks(2, C2)
result2 = matrix_multiply(blocks, K, n)
print('P2 = K^(-1) * C2 =', result2)
plain_text = "".join([(alp[int(round(digit) % n)]) for digit in result2])

print('Расшифрованное сообщение 2: ', plain_text)


