def f(x,y,A):
    return (3*x+y > 48) or (x > y) or (4*x+y<A)


for A in range(0,100):
    flag = False
    for x in range(0,100):
        for y in range(0,100):
            if f(x,y,A) == False:
                flag = True
                print(A)
                break

