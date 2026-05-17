f = open('primer_26.txt')
n = int(f.readline())

a = []
for i in range(n):
    a.append(int(f.readline()))

a.sort()

l = 0
r = n - 1
k = 0

while l < r:
    if a[l] + a[r] == 100:
        k = k + 1
        l = l + 1
        r = r - 1
    elif a[l] + a[r] < 100:
        l = l + 1
    else:
        r = r - 1

print(k)
f.close()
