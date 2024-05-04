

def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

count = 1
for i in range(245_690, 245_756+1):
    if isPrime(i) == True:
        print(i, count)
    count += 1

# ответ
"""
22 245711

30 245719

34 245723

52 245741

58 245747

64 245753
"""