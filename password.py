import random
import string

def gen_password():
    my_password = ""

    for i in range(10):
        my_password += random.choice(string.ascii_letters)
        print(my_password)

gen_password()