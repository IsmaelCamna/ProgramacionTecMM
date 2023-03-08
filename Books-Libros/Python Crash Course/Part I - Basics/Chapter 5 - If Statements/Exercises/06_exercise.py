"""
5.6 Stages of life

Write an if-elif-else chain that determines a person's
stage of life. Set a value for the variable age, then:

•   If the person is less than 2 years old, print a message that the person is a baby
•   If the person is at least 2 years old but less than 4, print message that
    the person is a toddler
•   If the person is at least 4 years old but less than 13, print a message that
    the person is a kid
•   If the person is at least 13 years old but less than 20, print a message that
    the person is a teenager
•   If the person is at least 20 years old but less than 65, print a message that
    the person is an adult
•   If the person is age 65 or older, print a message that the person is an
    elder
"""

age = 24

if age < 2:
    age = "baby"
elif age >= 2 and age < 4:
    age = "toodler"
elif age >= 4 and age < 13:
    age = "kid"
elif age >= 13 and age < 20:
    age = "teenager"
elif age >= 20 and age < 65:
    age = "adult"
else:
    age = "elder"
    
print("The person is a/an " + age)
