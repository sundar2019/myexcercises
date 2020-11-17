# math functions

print(round(3.5666,2))

#expression vs statement

iq=100
user_age = iq/5
print(user_age)

#augmented assignment operator
iq+=10
print(iq)

weather='It\'s sunny'
print(weather)

#formatted strings
name='sundar'
age=42
print(f'hi {name}.You are {age} old.')
print('hi {}.You are {} old.'.format(name,age))
print('hi {0}.You are {1} old.'.format(name,age))

#Developer fundatamentals
name = 'sundar'
age = 40
from datetime import date
birth_year=input('What year were you born? ')
current_date = date.today()
current_year =  current_date.year
age = int(current_year)-int(birth_year)
print ('Your age is ' + str(age))



#password_checker excercise

username=input("Enter your name here ")
password=input("Enter your password here ")
sec_pass=int(len(password))
# traditional way
print(username +" , Your password "+ ("*" * sec_pass) + " is " + str(sec_pass) + " letters long")
# using format 
print("{0} , Your Password {1} is {2} letters long".format(username,str("*"*len(password)), str(len(password))))

# cleaner way
sec_pass=int(len(password))
hidden_pass= "*"*sec_pass
print(f'{username} , your password {hidden_pass} is {sec_pass} letters long')

#lists 

amazon_cart=['notebooks','toys','gadgets','dresses','furniture']
print(amazon_cart[2])
print(amazon_cart[0:4:2])
print(amazon_cart)
amazon_cart[1]='electronics'
print(amazon_cart)
amazon_cart.append('grill')
print(amazon_cart)
amazon_cart.extend(['boat','cards'])
print(amazon_cart)
amazon_cart.pop()
print(amazon_cart)
t=amazon_cart.pop(3)
print(t)


