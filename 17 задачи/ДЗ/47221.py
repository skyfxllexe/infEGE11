f = open('47221.txt')
array = [int(i) for i in f]
maxim3 = 0
for i in range(len(array)):
    if abs(array[i]) % 10 == 3 and array[i] > maxim3:
        maxim3 = array[i]
count = 0
maxim = 0
for i in range(len(array)-1):
    if (array[i]**2 + array[i+1]**2 >= maxim3**2) and ((abs(array[i])%10 == 3) ^ (abs(array[i+1])%10 == 3)):
        count += 1
        maxim = max(maxim, array[i]**2 + array[i+1]**2)
print(count, maxim)

