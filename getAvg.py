import sys
#takes command line arguments in a array of strings

def addNumbers(num1, num2):
    return num1 + num2

def main():
    num1 = int(sys.argv[2])
    num2 = int(sys.argv[1])
    print(addNumbers(num1,num2))

main()
