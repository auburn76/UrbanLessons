first = float(input('Введите первое число '))
second = float(input('Введите второе число '))
third = float(input('Введите третье число '))

if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)
