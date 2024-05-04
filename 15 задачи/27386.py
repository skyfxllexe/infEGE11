def f(x,y,A):
    return (x*y<120) or (y>A) or (x>A)


for A in range(0,150):
    flag = True
    for x in range(0,100):
        for y in range(0,100):
            if f(x,y,A)==False:
                flag = False
                break

    if flag == True:
        print(A)