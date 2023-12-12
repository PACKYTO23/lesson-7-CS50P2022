# # # Trying to save input.

# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"Hello, {name}!")

# # # Saving input to a file.

# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# # # Reading files.

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("Hello", line.rstrip())

# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.rstrip())

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}.")
