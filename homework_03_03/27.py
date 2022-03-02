a = []
b = []
for i in range(11):
    a.append(i-8)
for j in range(11):
    b.append(a[j] + j)
print(a[2], b[9])