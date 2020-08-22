ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print(stuff.pop())
print(' '.join(stuff))

print(stuff.pop())
print(stuff)
print(stuff.pop())
print(stuff)
print(stuff.pop())
print(stuff)
print(stuff.pop()) # Even though we don't say stuff = stuff.pop(), it deletes the last element.
print(stuff)
print('#'.join(stuff[3:5])) # Wheras join doesn't join stuff permanently.
print(stuff)
