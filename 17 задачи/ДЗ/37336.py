

count = 0
maxim = 0
array = []
for i in range(len(array)-1):
    if array[i]%3 == 0 or array[i+1]% 3 == 0:
        count += 1
        if array[i] + array[i+1] > maxim:
            maxim = array[i] + array[i+1]

print(count, maxim)