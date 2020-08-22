def print_two(*two_args):
    arg1, arg2 = two_args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("Tigran", "Margaryan")
print_two_again("Tigran", "Margaryan")
print_one("Tigran")
print_none()
