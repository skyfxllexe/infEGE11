def f(x,A):
    return (x%A != 0) <= ((x%6==0) <= (x%4!=0))


for A in range(1,100):
    flag = True
    for x in range(1,100):
        if f(x,A) == False:
            flag = False
            break
    if flag:
        print(A)