#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: June 1, 2021
# The program will use one for loop and one if statement,
# outputting five integers per line with each separated by a space.


def fahrenheit():
    user_string = input("Enter the Temperature (°C): ")
    print("")

    # make sure if the user types anything but an integer, it's not valid
    try:
        user_int = int(user_string)
        print("")
    except ValueError:
        print("{} is not a integer" .format(user_string))

        # convert the tempertature in celsius from user into fahrenheit
    else:
        temp_to_f = (9/5)*user_int + 32
        print("{}°C is equal to {}°F". format(user_int, temp_to_f))

    finally:
        print("")

# call the function fahrenheit()


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
