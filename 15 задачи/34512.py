def f(x,A):
    return (x&77 != 0) <= ((x&12 == 0) <= (x&A!=0))

for A in range(0,100):
    flag = True
    for x in range(100):
        if f(x, A) == False:
            flag = False
            break
    if flag:
        print(A)