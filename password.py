#imports to generate random passwords and store them in strings

import random
import string

#write a function to generate a password
def gen_password():
    # my variable to store
    my_password = ""
    while len(my_password) < 10:

        for i in range(10):
            my_password += random.choice(string.ascii_letters)
            if i % 2 == 0:
                my_password += random.choice(string.ascii_letters)
                print(my_password)


gen_password()