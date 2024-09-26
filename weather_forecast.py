def temp_conversion():
    try:
        temp = float(temp_f)
        temp_c = (temp - 32) * 5 / 9
        if type(temp) != float:
            raise ValueError
    except ValueError:
        print(f"This is not a valid input. Please enter a valid number using digits.")
    else:
        print(f"{temp_f} degrees Fahrenheit is {temp_c:.2f} degrees Celcius.")
    finally:
        print("--- Weather Forecast Converter ---")


while True:
    temp_f = input("Enter todays temperature in Fahrenheit:\n")
    temp_conversion()

    continue_input = input("Would you like to try again? (yes/no):\n").strip().lower()
    if continue_input != "yes":
        print("Goodbye!")
        break
