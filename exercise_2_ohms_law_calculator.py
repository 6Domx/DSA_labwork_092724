# Pseudocode
# 1. Create an Ohm's Law calculator.
# 2. User should be able to choose wether to calculate Voltage, Current or Resistance.
# 3. Program should be able to use the Ohm's law to calculate missing variable and display the results.
# 4. Program should be able to handle cases wehre division by zero might occur.

def ohmlaw_calcu():
    print("What would you like to be calculated? Voltage (V), Current (I), or Resistance (R)?")
    variable = input("Enter V, I, or R: ").upper()

    if variable == 'V':
        i = float(input("Value of (I) in Amperes: "))
        r = float(input("Value of (R) in Ohms: "))
        v = i * r
        print(f"Voltage (V) = {v} Volts")
    elif variable == 'I':
        v = float(input("Value of (V) in Volts: "))
        r = float(input("Value of (R) in Ohms: "))
        i = v / r
        print(f"Current (I) = {i} Amperes")
    elif variable == 'R':
        v = float(input("Value of (V) in Volts: "))
        i = float(input("Value of (I) in Amperes: "))
        r = v / i
        print(f"Resistance (R) = {r} Ohms")
    else:
        print("Variable Selected is not valid. Please choose V, I, or R.")

ohmlaw_calcu()