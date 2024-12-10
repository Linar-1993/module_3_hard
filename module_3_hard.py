def calculate_structure_sum(*args):
    sum = 0
    for a in args:
        if isinstance(a, str):
            sum += len(a)
        elif isinstance(a, int):
            sum += a
        elif isinstance(a, float):
            sum += a
        elif isinstance(a, bool):
            sum += a
        elif isinstance(a, list):
            sum += calculate_structure_sum(*a)
        elif isinstance(a, tuple):
            sum += calculate_structure_sum(*a)
        elif isinstance(a, set):
            sum += calculate_structure_sum(*a)
        elif isinstance(a, dict):
            sum += calculate_structure_sum(*tuple(a.items()))
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)