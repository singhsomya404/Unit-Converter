# Unit Converter Tool in Python

def length_converter():
    print("\nLength Converter")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    print("3. Centimeters to Meters")
    print("4. Meters to Centimeters")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value * 1000, "meters")
    elif choice == 2:
        print("Result:", value / 1000, "kilometers")
    elif choice == 3:
        print("Result:", value / 100, "meters")
    elif choice == 4:
        print("Result:", value * 100, "centimeters")
    else:
        print("Invalid choice")


def weight_converter():
    print("\nWeight Converter")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value * 1000, "grams")
    elif choice == 2:
        print("Result:", value / 1000, "kilograms")
    else:
        print("Invalid choice")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter temperature: "))

    if choice == 1:
        result = (value * 9/5) + 32
        print("Result:", result, "°F")
    elif choice == 2:
        result = (value - 32) * 5/9
        print("Result:", result, "°C")
    else:
        print("Invalid choice")


# Main Program
while True:
    print("\n===== UNIT CONVERTER TOOL =====")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    print("4. Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        length_converter()
    elif option == 2:
        weight_converter()
    elif option == 3:
        temperature_converter()
    elif option == 4:
        print("Exiting Program...")
        break
    else:
        print("Invalid option! Please try again.")
