# run Python script using arguments in windows command line

import sys

def hello(name,num1,num2):
    print('Hello,',name,'!')
    print("That's your sum:", num1 + num2)

if __name__ == "__main__":
    name = str(sys.argv[1])
    num1 = int(sys.argv[2])
    num2 = int(sys.argv[3])
    hello(name,num1,num2)
