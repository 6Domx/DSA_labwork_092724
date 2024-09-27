# Pseudocode
# 1. Create a program that converts temperatures between Celsius and Fahrenheit
# 2. Ask the user to input a temperature
# 3. Ask the user to select the conversion type. Either Celsius to Fahrenheit or Fahrenheit to Celsius

def temperature_conversion():
    temp_input = float(input("Please enter the temperature you want to convert: "))
    ask_conversion = input("Do you want to convert it to Celsius or Fahrenheit? (C if Celsius, F if Fahrenheit): ")

    if ask_conversion == "F":
        fahrenheit = (temp_input * 9/5) + 32
        print(f"{temp_input}°C is converted to fahrenheit is {fahrenheit}°F")

    elif ask_conversion == "C":
        celsius = (temp_input - 32) * 5/9
        print(f"{temp_input}°F is converted to celsius is {celsius}°C")
    else:
        print("Please select either C or F only.")

temperature_conversion()