import random 
import string
password = ''.join(random.choice(string.printable) for i in range(8))
print(f"Randomised password |:| {password}")

