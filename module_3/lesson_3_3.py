def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(5,6,7)
print_params('Str', [4,5,6])
print_params(b = 25)
print_params(c = [1,2,3])
values_list = ['Four', 4, False]
values_dict = {'a': 15, 'b': 25, 'c': 35}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['Число', 22]
print_params(*values_list_2, 42)