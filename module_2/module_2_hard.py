import random

def get_result(key):
    result = []
    for i in range(1, key):
        for j in range(i, key):
            if key % (i + j) == 0:
                result.append([i, j])
    return result

#first_stone = int(input('Введите число на первом камне '))
first_stone = random.choice(range(3, 20))
print('Число на камне ', first_stone)
second_stone = get_result(first_stone)
print('Пара чисел ', second_stone)