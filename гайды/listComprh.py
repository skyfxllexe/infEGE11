f = open('1.txt')

# генераторы или list comprehensions 

n = int(f.readline())

array = [int(i) for i in f]
print(array)


# тернарные операторы

array = [i*i for i in range(1,100) if (i*i)%10 == 4]
print(array)