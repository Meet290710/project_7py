import datetime
import math
import random
import uuid
import time
import string
import custom_file_operations as file_ops


def datetime_operations():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            now = datetime.datetime.now()
            print("Current Date and Time:", now)

        elif choice == "2":
            date1 = input("Enter the first date (YYYY-MM-DD): ")
            date2 = input("Enter the second date (YYYY-MM-DD): ")

            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

            diff = abs((d2 - d1).days)
            print("Difference:", diff, "days")

        elif choice == "3":
            date_input = input("Enter date (YYYY-MM-DD): ")
            d = datetime.datetime.strptime(date_input, "%Y-%m-%d")
            print("Formatted Date:", d.strftime("%d-%B-%Y"))

        elif choice == "4":
            input("Press Enter to start stopwatch...")
            start = time.time()
            input("Press Enter to stop...")
            end = time.time()
            print("Elapsed Time:", round(end - start, 2), "seconds")

        elif choice == "5":
            seconds = int(input("Enter countdown time in seconds: "))
            while seconds:
                print("Time left:", seconds)
                time.sleep(1)
                seconds -= 1
            print("Time's up!")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


def math_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            num = int(input("Enter a number: "))
            print("Factorial:", math.factorial(num))

        elif choice == "2":
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))
            amount = p * (1 + r/100) ** t
            print("Compound Interest:", round(amount, 2))

        elif choice == "3":
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print("sin:", math.sin(rad))
            print("cos:", math.cos(rad))
            print("tan:", math.tan(rad))

        elif choice == "4":
            print("1. Circle")
            print("2. Rectangle")
            shape = input("Choose shape: ")

            if shape == "1":
                r = float(input("Enter radius: "))
                print("Area:", math.pi * r * r)
            elif shape == "2":
                l = float(input("Enter length: "))
                b = float(input("Enter breadth: "))
                print("Area:", l * b)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


def random_operations():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Random Number:", random.randint(1, 100))

        elif choice == "2":
            size = int(input("Enter list size: "))
            rand_list = [random.randint(1, 100) for _ in range(size)]
            print("Random List:", rand_list)

        elif choice == "3":
            length = int(input("Enter password length: "))
            chars = string.ascii_letters + string.digits + "@#$!"
            password = ''.join(random.choice(chars) for _ in range(length))
            print("Generated Password:", password)

        elif choice == "4":
            otp = random.randint(100000, 999999)
            print("Generated OTP:", otp)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


def generate_uuid():
    print("\nGenerate Unique Identifiers:")
    print("Generated UUID:", uuid.uuid4())


def explore_module():
    module_name = input("Enter module name to explore: ")
    try:
        module = __import__(module_name)
        print("Available Attributes in", module_name, "module:")
        print(dir(module))
    except:
        print("Module not found!")


def main():
    while True:
        print("\nWelcome to Multi-Utility Toolkit")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_operations()

        elif choice == "2":
            math_operations()

        elif choice == "3":
            random_operations()

        elif choice == "4":
            generate_uuid()

        elif choice == "5":
            while True:
                print("\nFile Operations:")
                print("1. Create a new file")
                print("2. Write to a file")
                print("3. Read from a file")
                print("4. Append to a file")
                print("5. Back to Main Menu")

                f_choice = input("Enter your choice: ")

                if f_choice == "1":
                    name = input("Enter file name: ")
                    file_ops.create_file(name)

                elif f_choice == "2":
                    name = input("Enter file name: ")
                    data = input("Enter data to write: ")
                    file_ops.write_file(name, data)

                elif f_choice == "3":
                    name = input("Enter file name: ")
                    file_ops.read_file(name)

                elif f_choice == "4":
                    name = input("Enter file name: ")
                    data = input("Enter data to append: ")
                    file_ops.append_file(name, data)

                elif f_choice == "5":
                    break

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
