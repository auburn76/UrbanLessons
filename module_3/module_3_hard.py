def calculate_structure_sum(n):
    #data_ = *n
    summa = 0
    for i in n:
        if isinstance(n[i], int) or isinstance(n[i], float):
            summa += n[i]
            return summa
        elif isinstance(n[0], str):
            summa += len(n[0])
            return summa
        else:
            calculate_structure_sum(*n[i])




data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)