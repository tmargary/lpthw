from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRl-C (^C).")
print("If you do want that, hit RETURN.")

input("?") # This is just a trick to stop the program here for an input of CTRl-C or RETURN.

print("Opening the file...")
target = open(filename, 'w') # OPEN

print("Truncating the file. Goodbye!")
target.truncate() # DELETE THE CONTENT

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1) # WRITE
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

txt = open(filename) # Opens the file for reading
print(f"Here's your file {filename}:")
print(txt.read()) # Reads the file
