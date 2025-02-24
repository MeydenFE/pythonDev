days = ["Mon", "Tue", "Wed"]
fruits = ["apple", "banana", "orange"]
drinks = ["coffee", "tea", "beer"]

# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

# zip関数で綺麗に描く リストの一番初めの値を取得することが出来る。
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
