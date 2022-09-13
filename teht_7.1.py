# Save the seasons as strings into a tuple in your program.

seasons_of_the_year = ("spring", "summer", "autumn", "winter")

# Write a program that asks the user for a number of a month and then prints out the corresponding season

month_number = int(input("Enter number of a month 1-12: "))

# We can define each season to last three months, December being the first month of winter.

if month_number == 12 or month_number == 1 or month_number == 2:
    print("It is " + seasons_of_the_year[3] + " season!")
elif month_number == 3 or month_number == 4 or month_number == 5:
    print("It is " + seasons_of_the_year[0] + " season!")
elif month_number == 6 or month_number == 7 or month_number == 8:
    print("It is " + seasons_of_the_year[1] + " season!")
elif month_number == 9 or month_number == 10 or month_number == 11:
    print("It is " + seasons_of_the_year[2] + " season!")
