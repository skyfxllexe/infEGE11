

f = open('37337.txt')

count = 0
maxim = -10e10

array = [int(i) for i in f]
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if (array[i] % 160 != array[j] % 160) and ((array[i]%7 == 0 ) or (array[j]%7) == 0):
            count += 1
            maxim = max(maxim, array[j] + array[i])
print(count, maxim)