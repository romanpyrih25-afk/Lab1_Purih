def convert_fahrenheit_to_celsius(temperature_fahrenheit):
    try:
        temp_f = int(temperature_fahrenheit)
        temperature_celsius = (temp_f - 32) * 5 / 9
    except ValueError:
        print("Please enter a valid temperature")
        return False
    return temperature_celsius


def run():
    is_running = True
    while is_running:
        user_input = input("Enter temperature in F: ")
        temp_c = convert_fahrenheit_to_celsius(user_input)

        if temp_c is not False:
            print(f"Temperature in C: {temp_c:.1f}")
            print("Do you want to proceed? (y/n)")
            choice = input()

            if choice == "y":
                is_running = True
            else:
                is_running = False
    return


if __name__ == '__main__':
    run()