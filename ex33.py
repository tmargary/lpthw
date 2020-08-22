i = 0
numbers = []

n = input("Choose n: ")
inc = input("Choose increment: ")

while i < int(n):
    print(f"At the top i is {i}")
    numbers.append(i)

    i += int(inc)
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
