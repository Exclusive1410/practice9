import numpy as np

# Матрицю 10x20 заповнити випадковими числами від 0 до 15. Вивести на екран саму матрицю і номера рядків, в яких число 5 зустрічається три і більше разів.
i = 0
j = 0
five = 0
arr = np.random.randint(0, 15, (10, 20))

while i < len(arr):
    while j < len(arr[i]):
        if arr[i][j] == 5:
            five += 1
        j += 1
    if five >= 3:
        print('Номер рядка в котором находиться 5 три и больше раз :' , i )
    i += 1
    j = 0
    five = 0
print(arr)