import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

random.shuffle(characters)

print(characters)