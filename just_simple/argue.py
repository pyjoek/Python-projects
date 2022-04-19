# from optparse import *
import optparse

parser = optparse.OptionParser(description="HELO THIS IS JOEL")

parser.add_option("-f","--first",dest="first",type=int, help="first number")
parser.add_option("-n","--new",dest="second",type=int, help="next number")

(options, arguments) = parser.parse_args()

first = options.first 
second = options.second

def numbers(m, n):
    print(m + n)

numbers(options.first, options.second)