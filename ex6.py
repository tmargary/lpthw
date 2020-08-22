type_of_people = 10
x = f"There are {type_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funnt?! {}"

print(joke_evaluation.format(hilarious)) # This code goes inside {} I guess. We will learn more about this later.

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
