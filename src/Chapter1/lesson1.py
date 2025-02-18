num: int = 1
name: str = "Mike"
is_ok = True

num = name

print(num, type(num))
# セミコロンで型を宣言しても上書きされてしまうので、あんま意味ない！

# print(name,type(name))
# print(is_ok,type(is_ok))

num = 1
name = "1"

new_name = int(name)
# print(new_name,type(new_name))
