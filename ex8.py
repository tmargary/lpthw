formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "The world's a little blurry",
        "Or maybe it's my eyes",
        "The friends I've had to bury",
        "They keep me up at night",
))
