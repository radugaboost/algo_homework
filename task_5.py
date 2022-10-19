import heapq

#программа принимает список чисел и номер элемента по убыванию
#выводит число под индексом k по убыванию
# O(n)

def findK(nums, k):
    q = heapq.nlargest(k, nums)
    return q[-1]
