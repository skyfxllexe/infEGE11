"""
Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. Назовём парой два идущих подряд элемента последовательности.
Определите количество пар чисел, произведение которых кратно 15, а их сумма делится на 7.
В ответе запишите два числа: сначала количество найденных пар, а затем  — максимальную сумму элементов таких пар.
"""

count = 0
maxim = -10e10 # - 10 * 10**10

f = open('39762.txt')

# большой код
array = []
for i in f:
    array.append(int(i))

for i in range(len(array)-1):
    if (array[i]*array[i+1])%15 == 0 and (array[i] + array[i+1]) % 7 == 0:
        count += 1
        if array[i] + array[i+1] > maxim:
            maxim = array[i] + array[i+1]
print(count, maxim)

# код поменьше немного

array = [int(i) for i in f]
for i in range(len(array)-1):
      if (array[i]*array[i+1])%15 == 0 and (array[i] + array[i+1]) % 7 == 0:
        count += 1
        maxim = max(maxim, array[i]+array[i+1])
print(count, maxim)

# самая короткая версия кода

array = [int(i) for i in f]
answer = [(array[i], array[i+1]) for i in range(len(array)-1) if (array[i]*array[i+1])%15 == 0 and (array[i]+array[i+1])%7 == 0]
print(len(answer))