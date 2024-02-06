color = input("Enter a color: ").capitalize()
if color == "Red" or color == "R" or color == "Blue" or color == "B" or color == "Yellow" or color == "Y":
    print("Your color is a primary color")
elif color == "Green" or color == "G" or color == 'Orange' or 'O' or color == "Purple" or color == "P":
    print("Your color is a secondary color")
else:
    print("Your input is not a primary or secondary color")
