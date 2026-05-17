f = open('primer_25.txt')
n, k, m = map(int, f.readline().split())

a = []
for i in range(n):
    a.append(int(f.readline()))

a.sort()

budget = a[:k]
s = 0
for x in budget:
    s = s + x
avg = s // k

premium = a[-m:]
mn = premium[0]
for x in premium:
    if x < mn:
        mn = x

print(mn, avg)
f.close()
