########################
# TASK 1: if, else, elif
########################

"""
Write a program that asks for a number between 1 and 7. The number serves as a
substitute for a day:
1 = Monday, 2 = Tuesday, ........, 7 = Sunday

The program should display a message (depending on the input!) on the screen:
a) "You have to work ...! (for Monday to Friday)
b) "Enjoy your weekend...! (for Saturday and Sunday)
c) "Wrong input...!" (for wrong number)
"""


daynumber = int(input("Input the day of Week: (1 = Montag, 2 = Dienstag, ..., 7 = Sonntag) "))

days = ["", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

if 1 <= daynumber <= 7:
    print("daynumber:", daynumber)
    print("day:", days[daynumber])

    if 1 <= daynumber <= 5:
        print("You have to work ...!")
    else:
        print("Enjoy the time now ...!")
else:
    print("Wrong input or do you live on another planet?")




########################
# TASK 2: if, else, elif
########################

"""
You have to divide your adult customers into 4 categories depending on their age.
Currently the following rules apply:

If: 18 <= customer_age < 25, category is: 'Youth'.
If: 25 <= customer_age  < 35, category is: 'YoungAdult'.
If: 35 <= customer_age < 60, category is: 'MiddleAged'.
If: 60 <= customer_age, category is: 'Senior'.

As an example, the following output is to be generated after the user has entered the age of the
customer (e.g. 22 year ) via 'input()':

"The customer belongs to the 'Youth' category!"
"""

age = input(" input your age:")
age = int(age)

if age <= 25 and age >= 18:
    print(f'{age} The customer belongs to the Youth category!')
elif age >= 25 and age <= 35:
    print("The customer belongs to the 'YoungAdult' category!")
elif age >= 35 and age <= 60:
    print("The customer belongs to the 'MiddleAged' category!")
else:
    print("The customer belongs to the 'Senior' category!")


########################
# TASK 3: if, else, elif
########################


"""
Your goal is to convert temperatures between the scales °Celsius and °Fahrenheit.

The centigrade scale, which is also called the Celsius scale, was developed by Swedish astronomer
Andres Celsius. In the centigrade scale, water freezes at 0 degrees and boils at 100 degrees.
The Fahrenheit scale was developed by the German physicist Daniel Gabriel Fahrenheit. In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees.

Equation relating the scales:

 T_C = (5/9) * (T_F - 32)

where T_C is the temperature in °Celsius and T_F is the temperature in °Fahrenheit.

Write two programs that will allow you to convert temperatures
a) from celsius to fahrenheit and
b) from fahrenheit to celsius.

Think about how you can combine the two programs in one program using a special input, e.g. F45
(for fahrenheit) or C23 (celsius)
"""


temperature = input("Input your temperature (e.g. 45F or 30C): ")
print(type(temperature))
unit = temperature[-1]
print(unit)
value_part = temperature[:-1]
print(value_part)


try:
     value = float(value_part)
except ValueError:
     print("Wrong format! Use e.g. 45F or 100C.")
     exit()

unit = temperature[-1].upper()
value_part = temperature[:-1]


# if value_part.replace(".", "", 1).isdigit():  # nokta varsa bir kez kaldır
#     value = float(value_part)
#     print("Numeric value:", value)
# else:
#     print("Wrong format! Use e.g. 45F or 100C.")
#     exit()

# "12.3.4".replace(".", "", 1) # "123.4" (sadece ilkini sildi)
# nokta silindikten sonra geriye sadece rakamlar kalıyor mu? sadece kontrol amaçlı
# eğer evet → demek ki sayı geçerli.


if unit == "F":
    celsius = (value - 32) * 5 / 9
    print(f"The temperature in Celsius is: {celsius:.2f}°C")
elif unit == "C":
    fahrenheit = value * 9 / 5 + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")
else:
    print("Wrong unit! Please use C or F.")


