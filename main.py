# 1
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        continue

# 2
for i in range(1, 51):
    if i % 5 == 0:
        print(i)
        continue

# 3
for i in range(-10, 11):
    if i < 0:
        continue
    print(i * 1, end=' ')

# 4
sum = 0
for i in range(1, 101):
    if i % 3 != 0:
        sum += 1
        continue
    print(sum)
