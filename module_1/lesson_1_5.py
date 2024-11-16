immutable_var = 1, 5, 'Top', True
print(immutable_var)
#immutable_var[1] = 4 - Кортеж не поддерживает обращение к элементу
mutable_list = [1, 5, 'Top', True]
print(mutable_list)
mutable_list[1] = 4
print(mutable_list)