array  = []
count = 0
maxim = 0
mean = sum(array) / len(array)

for i in range(len(array)-1):
    if (array[i]%5==0 or array[i+1]%5 == 0) and (array[i] < mean or array[i+1] < mean):
        count += 1
        if array[i] + array[i+1] > maxim:
            maxim = array[i] + array[i+1]

print(count, maxim)