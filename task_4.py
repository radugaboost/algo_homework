#Программа принимает на вход список чисел, находит минимальную разницу между двумя элементами
#После чего проверяет все элементы списка на эту минимальную разницу между ними и выводит подходящие пары
# O(n*log(n))

def min_diff(arr):
    arr.sort()
    min_diff = 10**6
    lst = []
    for i in range(1, len(arr)): ##определение минимальной разницы
        if arr[i] - arr[i-1] < min_diff:
            min_diff = arr[i] - arr[i-1]
    for i in range(1, len(arr)):  ##находим пары
        if arr[i] - arr[i-1] == min_diff:
            lst.append([arr[i-1], arr[i]])
    return lst
