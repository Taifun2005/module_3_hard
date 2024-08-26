data_structure = [
  [1, 2, 3],
  {'aфывапролд': 4, 'фывап': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


# summ = 0

def calculate_structure_sum(data_structure):
    # global summ
    summ = 0
    if isinstance(data_structure[0], list):               # list):  # Список
        for item in data_structure[0]:
            summ += item
        calculate_structure_sum(data_structure[1:])
    elif isinstance(data_structure[0], dict):  # dict): #Словарь
        for key in data_structure[0]:
            summ += len(key)  # Счет длины ключей
        print(*data_structure[0].values())
        calculate_structure_sum(data_structure[0])

            # #запустить функцию передав data_structure.values()
        # calculate_structure_sum(data_structure.values())

    elif isinstance(data_structure[0], int):
        summ += data_structure[0]
        calculate_structure_sum(data_structure[1:])
        return
    elif isinstance(data_structure[0], str):
        summ += len(data_structure[0])
        calculate_structure_sum(data_structure[1:])
        return

    elif isinstance(data_structure[0], tuple):          # tuple): #Кортеж
        for item in data_structure[0]:
            calculate_structure_sum(data_structure[0][item])
            summ += calculate_structure_sum(item)
    elif isinstance(data_structure[0], set):            # set):  # Множестро
        for item in data_structure[0]:
            calculate_structure_sum(data_structure[0][item])
            summ += calculate_structure_sum(item)




result = calculate_structure_sum(data_structure)
print(result)

