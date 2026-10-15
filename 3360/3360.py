"""hello"""
w, h, m, n = map(int, input().split())
if not m and not n:
    pass
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = [0] + sorted(x) + [w]
y = [0] + sorted(y) + [h]

maxvre = []
for i in range(1, len(x)):
    diff = x[i] - x[i - 1]
    maxvre.append(diff)
maxvre.sort(reverse=True)

kimi = []
for i in range(1, len(y)):
    diff = y[i] - y[i - 1]
    kimi.append(diff)
kimi.sort(reverse=True)

w1 = maxvre[0]
w2 = maxvre[1]
h1 = kimi[0]
h2 = kimi[1]

ok = w1 * h1
ok2 = max(w1 * h2, w2 * h1)

print(ok, ok2)
