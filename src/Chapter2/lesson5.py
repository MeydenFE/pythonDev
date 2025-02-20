seat = []
min = 0
max = 5
min <= len(seat) < max
print(min <= len(seat) < max)


seat.append("P")
print(min <= len(seat) < max)

seat.append("P")
seat.append("P")
seat.append("P")
print(min <= len(seat) < max)

seat.append("P")
print(min <= len(seat) < max)
print(len(seat))

seat.pop(0)
print(min <= len(seat) < max)
