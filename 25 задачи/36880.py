
array = []

for m in range(0,51, 2):
    for n in range(1,51,2):
        number = (2**m) * (3**n)
        if number >= 400_000_000 and number<=600_000_000:
            array.append(number)


print(*sorted(array), sep='\n')