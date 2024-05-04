# найти все делители числа быстро
import datetime


# код, время работы которого измеряем

#фиксируем и выводим время окончания работы кода




# наивная реализация. complexity O(n)
def divs(n):
    dividers = []
    for i in range(1,n+1):
        if n%i == 0:
            dividers.append(i)

    return dividers

start = datetime.datetime.now()
print('Время старта: ' + str(start))

print(divs(100000000))
finish = datetime.datetime.now()
print('Время окончания: ' + str(finish))


# вычитаем время старта из времени окончания
print('Время работы: ' + str(finish - start))   
# быстрая реализация. complexity O(sqrt(n))

def divs_2(n):
    dividers = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            dividers.append(i)
            if n//i != i:
                dividers.append(n//i)

    dividers.sort()
    return dividers

start = datetime.datetime.now()
print('Время старта: ' + str(start))

print(divs_2(1000000000))
finish = datetime.datetime.now()
print('Время окончания: ' + str(finish))


# вычитаем время старта из времени окончания
print('Время работы: ' + str(finish - start))   
