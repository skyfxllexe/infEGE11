# Перебрать все пары чисел в массиве


array = [1,2,3,4,5,6,7,8,9]

for i in range(len(array)):
    for j in range(i+1, len(array)):
        print(array[i], array[j])

# это перебирает все пары

# перебрать пары, рядом стоящие, то есть все i, j: j-i = 1

for i in range(len(array)-1):
    print(array[i], array[i+1])
 
# пример для тройки рядом стоящих + альтернатива диапазонов
for i in range(2,len(array)):
    print(array[i], array[i-1], array[i-2])

# хочется, перебрать все пары, i,j, такие что j-i >= k

k = int(input())
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if j-i >= k: # иногда <= нужно расстояние не больше k, или строгое неравенство
            print(array[i], array[j])


    