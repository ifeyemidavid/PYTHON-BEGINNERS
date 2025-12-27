import sys

username = "JCS"
print("my name is",username)


name = input("what is your name?")
print("hello", name)


surname = input("Enter your Surname: ")
age = input("Enter your age: ")

print(f"Hello, {surname}! you are {age} years old.")

#converting input strings to numeric types

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

print(f"sum: {num1 + num2}")
print(f"sum: {num1 - num2}")
print(f"sum: {num1 * num2}")

if num2 != 0:
    print(f"quotient: {num1 / num2}")
else :
    print("cannot divide by zero.")

 
def main():
    if len(sys.argv) != 3:
        print("usage: python area.py length width")
        sys.exit(1)

    try:
        length = float(sys.argv[1])
        width = float(sys.argv[2])
        area = length * width
        print(f"Area of rectangle: {area}")
    except ValueError:
        print("length and width must be numeric")

main()
        


