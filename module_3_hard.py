data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


# summ = 0
def calculate_structure_sum(data_structure):
    # global summ
    total_sum = 0
    for i in range(0, len(data_structure)):
        # for i in len(data_structure):
        if isinstance(data_structure[i], (list, tuple, set)):  # list):  # списком, кортежем или множеством
            if isinstance(data_structure[i], set):
                total_sum += calculate_structure_sum(list(data_structure[i]))
            else:
                total_sum += calculate_structure_sum(data_structure[i])
        elif isinstance(data_structure[i], dict):  # dict): #Словарь
            total_sum += calculate_structure_sum([*(data_structure[i]).values()])
            total_sum += calculate_structure_sum([*(
            data_structure[i]).keys()])  # на результат рекурсивного вызова функции с элементами словаря (arg.items()).
        elif isinstance(data_structure[i], str):
            total_sum += len(data_structure[i])
        elif isinstance(data_structure[i], (int, float)):
            total_sum += data_structure[i]
    return total_sum


result = calculate_structure_sum(data_structure)
print(result)


# data_structure = [
#   [1, 2, 3],
#   {'aфывапролд': 4, 'фывап': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# def calculate_structure_sum(data_structure):
#
#
#
#
# result = calculate_structure_sum(data_structure)
# print(result)


#     for item in data_structure[0]:
#         summ += item
#     elif
    #
    # if isinstance(*data_structure[0], list):               # list):  # Список
    #     for item in data_structure[0]:
    #         summ += item
    #     calculate_structure_sum(data_structure[1:])
    # elif isinstance(data_structure[0], dict):  # dict): #Словарь
    #     for key in data_structure[0]:
    #         summ += len(key)  # Счет длины ключей
    #     for values in data_structure[0].values():
    #         summ += values
    #     calculate_structure_sum(data_structure[1:])
    # elif isinstance(data_structure[0], tuple):          # tuple): #Кортеж
    #     for item in data_structure[0]:
    #         summ += item
    #         calculate_structure_sum(data_structure[1:])
    #         # calculate_structure_sum(data_structure[1:][item])
    # elif isinstance(data_structure[0], str):
    #     summ += len(data_structure[0])
    #     calculate_structure_sum(data_structure[1:])
    #     return
    #
    #
    # elif isinstance(data_structure[0], int):
    #     summ += data_structure[0]
    #     calculate_structure_sum(data_structure[1:])
    #     return
    #
    #
    # elif isinstance(data_structure[0], set):            # set):  # Множестро
    #     for item in data_structure[0]:
    #         calculate_structure_sum(data_structure[0][item])
    #         summ += calculate_structure_sum(item)







# data_structure = [[1, 2, 7],[3,5]]
# summ = 0
# def calculate_structure_sum(data_structure):
#     global summ
#     print(*data_structure)
#     k = len(data_structure)-1
#     if isinstance(data_structure[0], int):
#         if k == 0:
#             summ += data_structure[0]
#             return
#         else:
#             summ += data_structure[0]
#             calculate_structure_sum(data_structure[0][1:])
#             return summ
#
# print(f"result : {calculate_structure_sum(data_structure)}")








'''data_structure = [1, 2, 3, 4, 5, 6]
summ = 0
def calculate_structure_sum(data_structure):
    global summ
    k = len(data_structure)-1
    if isinstance(data_structure[0], int):
        if k == 0:
            summ += data_structure[0]
            return
        else:
            summ += data_structure[0]
            calculate_structure_sum(data_structure[1:])
            return summ

print(f"result : {calculate_structure_sum(data_structure)}")
'''