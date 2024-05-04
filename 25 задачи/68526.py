"""
 3?12?14*5
числа НЕ ПРЕВЫШАЮТ 10^10
почему это важно? 
потому что * - подразуемвает любое количество символов, то есть ВООБЩЕ любое

3?12?14*5
10000000000
сколько можно вместо звездочки?
можно: ничего, одну цифру, две цифры
"""

# 1 случай. Звезда - пустая

for a in range(0,10):
    for b in range(0,10):
        number = int(f'3{a}12{b}145')
        if number % 1917 == 0:
            print(number)

# 2 случай. Звезда - суть символ (1 символ)


for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            number = int(f'3{a}12{b}14{c}5')
            if number % 1917 == 0:
                print(number)


# 3 случай. Звезда - две цифры
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                number = int(f'3{a}12{b}14{c}{d}5')
                if number % 1917 == 0:
                    print(number)

