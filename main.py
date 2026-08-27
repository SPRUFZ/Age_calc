# Age Calculator start intro into asking questions
print("Welcome to your profile & age calculator")
print("I'm going to ask you a some questions about you.")
print("Then I'll calculate exactly how long you have been alive for including leap years")
#ask questions to find variable
print("What's your name?")
name = input("enter your name: ")
print(f"Hello, {name}!")

print("Now what year were you born?")
birth_year = int(input("enter the year you were born: "))
print(f"Great! So you were born in {birth_year}.")

print("Now what month were you born?")
birth_month = (input("enter the name of the month you were born: "))
print(f"Great! So you were born in {birth_month}.")

print("Now what day were you born?")
birth_day = int(input("enter the day you were born: "))
print(f"Great! So you were born on the {birth_day}th of {birth_month} in {birth_year}.")

print("whats your favorite food?")
favorite_food = input("enter your favorite food: ")
print(f"{favorite_food} is hella yum")

print("whats your favorite hobby?")
favorite_hobby = input("enter your favorite hobby: ")
print(f"{favorite_hobby} sounds lame loser")

print("whats your favorite color?")
favorite_color = input("enter your favorite color: ")
print(f"{favorite_color} is a pretty color")

print("whats your favorite animal?")
favorite_animal = input("enter your favorite animal: ")
print(f"{favorite_animal} is a pretty cool animal")
print("where yo crib located at?")
where_yo_crib_located_at = input("enter your city: ")
print(f"so you live in {where_yo_crib_located_at}? that's a bum ahh place to live")
#birth year is current date - birth year is the age
age = 2026 - birth_year 
print("")
print(f"{name}'s time alive calculator:")
#calculations for all age time variables
print(f"{age} years old")
# days included with leap years is age times 365 + leap years. which was age divided by 12
leap_years = (age // 4)
print(f"{age * 12} months old")
print(f"{age * 365 + leap_years} days old")
print(f"{age * 365 * 24} hours old")
print(f"{age * 365 * 24 * 60} minutes old")
print(f"{age * 365 * 24 * 60 * 60} seconds old")
print("")
print(f"{name}'s profile:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Hobby: {favorite_hobby}")
print(f"City: {where_yo_crib_located_at}")
print(f"Favorite Color: {favorite_color}")
print(f"Favorite Animal: {favorite_animal}")
print("")
print("Thanks for using my profile & age calculator!")
print("I hope you enjoyed it and learned something new about yourself!")
#end of code should have no flaws and answer all questions with the variables you typed in.
