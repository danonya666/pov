a = [1,2, 5, 765, 756765,4, 324, 32]
b = [1,2, 5, 765, 756765, 1488, 4, 324, 32, ]
res = 0
for i in a:
    res ^= i

for i in b:
    res ^= i

print(res)