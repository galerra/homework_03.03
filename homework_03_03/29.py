c = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j - 3 <= 0:
            c += 1
print(c)
