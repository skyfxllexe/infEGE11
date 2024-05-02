f = open('27686.txt')

s = f.read()
cur_len = 0
maxim = 0

for i in range(len(s)):
    if s[i] == 'X': # не русскую Х проверять, а латинскую
        cur_len += 1
    else:
        maxim = max(maxim, cur_len)
        cur_len = 0

print(maxim)


# 2 способ


print(s.count("XXXXXXXXXXXXXXXXXXX"))
print(len('XXXXXXXXXXXXXXXXXXX'))


# 3 способ