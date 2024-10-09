import random

letters  = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


# FIRST METHOD

# rand_letters = []
# rand_numbers = []
# rand_symbols = []
#
# for i in range(0, nr_letters):
#     rand_letters.append(letters[random.randint(0, len(letters)-1)])
#
# for i in range(0, nr_symbols):
#     rand_symbols.append(symbols[random.randint(0, len(symbols) -1 )])
#
# for i in range(0, nr_numbers):
#     rand_numbers.append(numbers[random.randint(0, len(numbers) -1 )])
#
# print(rand_letters)
# print(rand_numbers)
# print(rand_symbols)
#
# total_len = len(rand_symbols) + len(rand_numbers) + len(rand_letters)
#
# print(total_len)
#
# for i in range(0, len(rand_numbers)):
#     rand_letters.insert(random.randint(0, len(rand_letters)-1), rand_numbers[random.randint(0, len(rand_numbers)-1)])
#
# for i in range(0, len(rand_symbols)):
#     rand_letters.insert(random.randint(0, len(rand_letters)-1), rand_symbols[random.randint(0, len(rand_symbols)-1)])
#
# print("".join(rand_letters))

#SECOND METHOD

password_list = []

for i in range(0, nr_letters):
    password_list.append(random.choice(letters))

for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = "".join(password_list)
print(password)