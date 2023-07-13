from random import randit

number = (1, 6)
print("Ok, I've thought of a number 1 and 6,\n")
prompt = "Make a Guess: "
answer = -1

while answer != number
    answer = int(input(prompt))
    if answer < number:
        print("That's too low.\n")
    elif answer > number
        print("That's too high.\n")
