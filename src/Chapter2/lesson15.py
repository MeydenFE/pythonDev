# 共通点を見つけ出すときは集合型が便利

my_frineds = {"A", "B", "C"}
A_frineds = {"B", "D", "E", "F"}
print(my_frineds & A_frineds)

# リストを集合に型を変える
f = ["apple", "banana", "apple", "banana"]
kind = set(f)
print(kind)
