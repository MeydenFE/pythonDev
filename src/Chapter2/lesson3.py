r = [1, 2, 3, 4, 5, 1, 2, 3]

print(r.index(3, 3))

# カウント
print(r.count(3))

if 5 in r:
    print("exist")

# ソート機能
r.sort()
print(r)
r.reverse()
print(r)

r.reverse()
print(r)

s = "My name is Mike."
to_split = s.split(" ")
print(to_split)

x = " ".join(to_split)
print(x)

w = "MyName isYu."
to_slitYu = w.split(" ")
print(to_slitYu)

w = " ".join(to_slitYu)
print(w)

print(help(list))
