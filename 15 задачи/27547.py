def f(x,y,a):
    return (3*x + 5*y < a) or (x>=y) or (y>8)



for A in range(1,100):
    flag = True
    for x in range(100):
        for y in range(100):
            if f(x,y,A) == False:
                flag = False
                break
    if flag == True:
        print(A)