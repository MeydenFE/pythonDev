t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))

# t[0] = 100
# print(t)

print(t[-1])
print(t.count(1))

# print(help(t))

# タプル型は読み込み用のイメージ

t = ([1, 2, 3], [4, 5, 6])
print(t, type(t))

t = (1,)

print(type(t))

t = ()
print(type(t))

t = 1
print(type(t))

t = ("test",)
print(type(t))

new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)

new_tuple = (1,) + (4, 5, 6)
print(new_tuple)
