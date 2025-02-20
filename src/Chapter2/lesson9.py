d = {"x": 10, "y": 10}
print(d, type(d))

print(d["x"])

d["x"] = 100
print(d, type(d))

d["x"] = "XXXXX"
print(d, type(d))

d["z"] = 200
print(d, type(d))

d[1] = 10000
print(d, type(d))

print(dict(a=10, b=20))
print(dict([("a", 10), ("b", 20)]))
