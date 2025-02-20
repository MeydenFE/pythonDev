i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print("j=", j)
print("i=", i)

x = [1, 2, 3, 4, 5]
# y = x.copy()
y = x[:]

y[0] = 100
print("y=", y)
print("x=", x)

X = 20
Y = X
Y = 5
print(X, Y)

print(id(X))
print(id(Y))

X = ["a", "b"]
Y = X
Y[0] = "p"
print(X, Y)

print(id(X))
print(id(Y))

# リスト型は🟰で結ぶと、同じIDになるので、値私渡しは気を付ける。
