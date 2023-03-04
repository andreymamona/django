import datetime
import time


def task16(start: int, end: int) -> list[int]:
    """
    Два натуральных числа называют дружественными, если каждое из них равно
    сумме всех делителей другого,
    кроме самого этого числа. Реализовать функцию для поиска всех пар
    дружественных чисел в заданном диапазоне
    """
    t_start = time.time()

    def summa(m: int):
        summ = 1
        for i in range(2, int(m / 2) + 1):
            if m % i == 0:
                summ += i
        return summ
    friend = []
    for j in range(start, end + 1):
        a = summa(j)
        b = summa(a)
        if b == j != a:
            friend.append(j)
            print(t_start - time.time())
    print(t_start - time.time())
    return friend


print(task16(1, 20000))
