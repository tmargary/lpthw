from sys import argv

script, filename = argv # This line is for inputing the file name

txt = open(filename) # Opens the file for reading

print(f"Here's your file {filename}:")
print(txt.read()) # Reads the file

print("Type the filename again:") # Same happens here using input()
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
