def main():
    print("Welcome to the Python Greeter & Summer!")

    name = input("What is your name? ")
    print(f"Hello, {name}!")

    try:
        num1 = float(input("Enter the first number to sum: "))
        num2 = float(input("Enter the second number to sum: "))
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is {total}.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()