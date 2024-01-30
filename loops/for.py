# names = ["Ben", "Jon", "Mike", "Jona"]

# for name in names:
#     if name == "Jona":
#         break
#     print(name)


# range
for x in range(10):
    print(x)

# range - start and stop
for x in range(2, 4):
    print(x)

# range - steps
for x in range(0, 101, 5):
    print(x)
else:
    print("loop is over")


# timetable
table_number = int(input("Enter table number: "))

for i in range(1, 13):
    result = i * table_number
    print(f"{i} x {table_number} = {result}")
