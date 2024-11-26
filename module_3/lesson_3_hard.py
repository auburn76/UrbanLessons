def calculate_structure_sum(*args):
    summa = 0
    for i in args:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            summa += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            for key, value in i.items():
                summa += calculate_structure_sum(key, value)
        elif isinstance(i, int) or isinstance(i, float):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
    return summa

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)