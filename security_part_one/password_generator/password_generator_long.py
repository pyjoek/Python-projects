import random
import datetime
import optparse, os

parser = optparse.OptionParser(description="create random password")

parser.add_option("-f","--file name",dest = "file",help = "Enter the file name")

(options, argument) = parser.parse_args()

file = options.file

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/_-'\"!@#$%^&+"

ally = lower + upper + numbers +symbols

length = 16

password = "".join(random.sample(ally, length))

a = datetime.datetime.now()
print(a)

with open(f"{options.file}","w") as fil:
    fil.write(f'''
    +----------+-+----------------+-+----------------+-+-----+------------------------+
    | password |:| {password} |:| was created at |:| {a} |
    +----------+-+----------------+-+----------------+-+-----+------------------------+
    ''')

with open(f"{options.file}") as fil:
    print(fil.read())
# print(password)