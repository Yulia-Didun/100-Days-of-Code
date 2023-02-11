#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
num_of_letters= int(input("How many letters would you like in your password?\n")) 
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))


total_list = [letters, symbols, numbers]
password = []

#for num in range(0, num_of_letters):
#    new_letter = random.randint(0, len(letters)-1)
#    password.append(letters[new_letter])
#for num in range(0, num_of_symbols):
#    new_symb = random.randint(0, len(symbols)-1)
#    password.append(symbols[new_symb])
#for num in range(0, num_of_numbers):
#    new_num = random.randint(0, len(symbols)-1)
#    password.append(numbers[new_num])


for char in range(0, num_of_letters):
    password.append(random.choice(letters))

for char in range(0, num_of_symbols):
    password.append(random.choice(symbols))

for char in range(0, num_of_numbers):
    password.append(random.choice(numbers))


random.shuffle(password)

print(f"Here is your password: {''.join(password)}")