f = open('primer_27.txt')
n = int(f.readline())

a = []
for i in range(n):
    a.append(int(f.readline()))

s = 0
for x in a:
    s = s + x
avg = s / n

b = sorted(a)
med = b[n // 2]

if avg < med:
    low = avg
    high = med
else:
    low = med
    high = avg

k = 0
for x in a:
    if low <= x <= high:
        k = k + 1

print(k)
f.close()
