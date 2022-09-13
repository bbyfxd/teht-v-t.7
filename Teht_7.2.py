# Write a program that asks the user to enter names until he/she enters an empty string.

keep_going = True
while keep_going:
    name = input("Enter names, or enter an empty string to quit: ")
    if name == "":
        keep_going = False

# After each name is read the program either prints out New name
# or Existing name depending on whether the name was entered
# for the first time.


# Finally, the program lists out the input names one by one,
# one below another in any order. Use the set data structure to store the names.
