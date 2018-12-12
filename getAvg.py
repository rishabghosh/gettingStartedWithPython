import sys
#takes command line arguments in a array of strings

def addNumbers(num1, num2):
    return num1 + num2

def main():
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print(addNumbers(num1,num2)/2)

main()
