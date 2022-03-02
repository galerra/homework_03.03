l_1 = []
l_2 = []
for i in range(101):
    l_1.append(300 - i * 100)
for j in range(101):
    l_2.append(l_1[j] + 200)

c = 0
for l_1 in l_2:
    if l_1 < 0:
        c += 1
print(c)
