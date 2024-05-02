

"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
Определите символ, который чаще всего встречается в файле сразу после буквы A.
"""

f = open('33196.txt')
s = f.read()
myDict = dict()

for i in range(len(s)-1):
    if s[i] == 'A':
        if not(s[i+1] in myDict.keys()):
            myDict[s[i+1]] = 0
        myDict[s[i+1]] += 1

maxim_index = 0
maxim_value = 0

for i in myDict.keys():
    if myDict[i] > maxim_value:
        maxim_value = myDict[i]
        maxim_index = i
print(maxim_index)


# HASH-MAP, dictionary, ordered_hash_map, unordered_hash_map