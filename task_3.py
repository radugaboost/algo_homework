#Программа получает строку с ключевыми символами и строку с символами
#в которой нужно найти количество ключевых символов
#выводит количество ключевых символов
# O(log(n))

def jewels_and_stones(jewels, stones):
    x = set(jewels) #уникальные элементы
    cnt = 0
    for i in stones:
        if i in x:
            cnt += 1
    return cnt
