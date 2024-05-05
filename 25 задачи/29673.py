def divs(n):
    dividers = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            dividers.append(i)
            if n//i != i:
                dividers.append(n//i)

    dividers.sort()
    return dividers



for i in range(int(123456789**0.5), int(223456789**0.5)+1):
    if len(divs(i)) == 3:
        print(i*i, int(i*(i**0.5)))

# мы ищем простые числа в четвертой степени
# p^4. p^3

# i = p^2. p^3 = p^2 * p
# p = sqrt(i)