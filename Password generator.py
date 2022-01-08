import random
import string
print("Welcome to our Random Password Generator")
length=int(input("Enter the length of password you want: "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
temp = random.sample(all,length)
password = "".join(temp)
print(password)