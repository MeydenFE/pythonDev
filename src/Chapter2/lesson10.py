d = {"x": 10, "y": 20}
print(d.keys())
print(d.values())

dict_values = [10, 20]
d2 = {"x": 1000, "j": 500}
print(d, d2)

d.update(d2)
print(d)

# print(d["z"])
print(d.get("x"))

d.pop("x")
print(d, d2)

del d["y"]
print(d, d2)

d.clear()
print(d)

d = {"x": 10, "y": 20}
print("a" in d)
