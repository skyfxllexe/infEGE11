# на отрезке найти числа у которых ровно 4 делителя


def divs(n):
    dividers = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            dividers.append(i)
            if n//i != i:
                dividers.append(n//i)

    dividers.sort()
    return dividers


for i in range(185_311, 185_330+1):
    # как измерить количество делителей, нося на руках функцию, которая возвращает массив делителей?
    if len(divs(i)) == 4:
        print(divs(i))