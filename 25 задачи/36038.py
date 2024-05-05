


def divs(n):
    dividers = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            dividers.append(i)
            if n//i != i:
                dividers.append(n//i)

    dividers.sort()
    return dividers
count = 0
for i in range(452_022, 1_000_000):
    if len(divs(i))<=2:
        M = 0
    else:
        M = divs(i)[1] + divs(i)[-2]
        if M%7 == 3:
            count += 1
            print(i, M)
            if count == 5:
                break
            
