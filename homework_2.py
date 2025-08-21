import numpy as np

#Завдання 1#
array_one = ([1, 2, 3])
array_two = ([4, 5, 6])

result = np.hstack((array_one, array_two))

print("Результат першого завдання:", result)

#Завдання 2#
array = np.array([12, -5, 7, 9, -3, 15])

result = np.append(array, 10)

print("Результат другого завдання:", result)

#Завдання 3#
array = np.array([
    [5, 2, 8],
    [1, 7, 4],
    [3, 6, 9]
])

result = np.delete(array, 1, axis=0)

print("Результат третього завдання:", result)