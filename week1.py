import datetime
current_year=datetime.datetime.now().year

#Section1

print ("Section1")
name = "Olena"
age = 43
height = 5.8
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section2
print ("Section2")
user_name = input("Please enter your name: ")
user_year = input("Please enter the year you were born: ")

print (f"Hi, {user_name}! You are approximately {current_year - int(user_year)} years old.")

#Section3
print ("Section3")
number1 = float(input ("Please enter the first number: "))
number2 = float (input ("Please enter the second number: "))

print (f"The result: {number1} * {number2} = {number1 * number2}.")

#Secion4
print ("Section4")
item = "Python textbook"
price = 38.56
quantity = 10

print (f"""===========================
        RECEIPT
===========================
Item:      {item}
Price:     ${price}
Quantity:  {quantity}
---------------------------
Total:     ${price * quantity}
===========================  
""")

#Secion5
print ("Section5")

user_full_name = input("Please enter your full name: ")
user_hometown =  input("Please enter your hometown: ")
user_hobby =  input("Please enter your hobby: ")
user_fun_fact =  input("Please enter one fun fact about yourselves: ")
user_born_year =  input("Please enter the year you were born: ")

print (f"""
╔═══════════════════════════════════╗
      PROFILE: {user_full_name}
╚═══════════════════════════════════╝
Hometown:   {user_hometown}
Hobby:      {user_hobby}
Fun fact:   {user_fun_fact}
Age:        {current_year - int(user_born_year)}
""")


