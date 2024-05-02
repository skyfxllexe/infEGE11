


f = open('27421.txt')
s = f.read()
cur_len = 1
maxim = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cur_len += 1
    else:
        maxim = max(maxim, cur_len)
        cur_len = 1
print(maxim)