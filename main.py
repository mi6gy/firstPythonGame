print("Welcome to my first python game.\n")

# user inputs
name = input("What is your name? ")
print("Hello " + name)
age = int(input("What is your age? "))
print("Hello", name, "you are", age, "years old.\n")

#check if player is old enoguh to play using conditions

if age >= 18:
    print("You are old enough to play.")

    wants_to_play = input("Are you sure you want to play? Shall we begin?").lower()
    if wants_to_play == "yes":
        print("Let's begin...\n")
else:
    print("You're not old enough to participate")


'''
DATA TYPES
str = anthing inside single or double quotation marks. a collection of characters or text. used to print
int = any whole number. 1,4,7,235,-13
float = any number with floating decimal point 4.5,2.0, -100.01
bool = true or false
'''
