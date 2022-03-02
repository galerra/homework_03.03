a = 7
l_1 = [2] * a
for i in range(a):
    l_1[i] = [2]*a
for i in range(a):
    l_1[i][2] = l_1[i][2]*2
for i in range(a):
    l_1[5][i] = l_1[5][i] + 3*i
print(l_1[5][2])