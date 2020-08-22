from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) # The index od the character you wanna go back to
    # I guess we have to go back (rewind) to print anything.
    # seek(0) goes back to the 0'th character in order to print it again.
    # seek(0) goes back to 1'th character
    # seek is dealing with bytes, not lines

def print_a_line(line_count, f):
    print(line_count, f.readline()) # readline does what it says (until it findes the \n)

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.") # I guess we have to go back (rewind) to print anything.

rewind(current_file) # Hence, rewind

print("Let's print three lines")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
