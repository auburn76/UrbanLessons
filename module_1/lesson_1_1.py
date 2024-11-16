example='обучение'
print(example[0])
print(example[-1])
length_half_string=len(example)//2
if (len(example)-length_half_string) % 2 == 0: #проверяем, что вторая часть слова чётная
    length_half_string=length_half_string+1 #если чётная, укорачиваем на один символ
print(example[length_half_string:])
print(example[::-1])
print(example[1::2])