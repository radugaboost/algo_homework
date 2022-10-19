#Программа принимает минимальное число, максимальное число и проверяет интервал между ними (включая их)
#проверяет мощность числа (кол-во шагов для того, чтобы привести его к 1)
#если нечетное - умножаем на 3 и прибавляем 1
#если четное - делим на 2
#по мощности числа сортируются в библиотеке
#затем выводится k-й элемент
# O(n*log(n))


def getKth(lo, hi, k):
        def power_value(x):
            dict = {}
            num, result = x, 0
            while x > 1 and x not in dict:
                result += 1
                if x%2 == 0:
                    x //=2
                else:
                    x = 3*x + 1
            dict[num] = result + (dict[x] if x > 1 else 0)
            return dict[num], num
        
        return sorted(range(lo, hi+1), key=power_value)[k-1]
