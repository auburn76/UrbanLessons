def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)

'''
В задании показан пример, где result2 также возвращает 24. Считаю, что это не верно, т.к при команде
int ноль игнорируется если за ним есть другие цифры. Если число заканчивается на "0", то при последнем
выполнении get_multiplied_digits переменная first будет равна "0". В задании не указано, что последний
"0" надо игнорировать. При умножении на "0" произведение будет равно "0"
'''