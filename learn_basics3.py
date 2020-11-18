#Loops
'''
#for item in 'Zero to Masgtery':
for item in (1,2,3,4,5):
  print(item)


for item in (1,2,3,4,5):
  for x in ['a','b','c']:
    print(item,x)
'''
# Iterating Dictionaries
user ={
  'name': 'sundar',
  'age': 40,
  'company': 'TCS'
  }
for item in user:
   print(item)
for item in user.items():
   print(item)

for key,value in user.items():
  print(key, value)
for item in user.keys():
  print(item)
for item in user.values():
  print(item)


#counter
my_list=[1,2,3,4,5,6,7,8,9,10]
k=0
for i in my_list:
  k=k+i
print(k)
  
# range
for i in range(2,15,3):
  print(i)

for i in range(10,0,-1):
  print(i)

#enumerate
for char in enumerate('Hello'):
  print(char)

for i,char in enumerate(list(range(100))):
  if(char == 50):
    print('The index of {0} is {1}'.format(char,i))
 

#While Loops
i=0
while i <5:
  i=i+1
  print(i)
  break


#parameters
def say_hello(name='Kavi',age=38):
  print(f'helloooo {name} {age}')
  
#positional arguments
say_hello('Sundar','40')

#keyword arguments
say_hello(age=30,name='Shan')

#default parameters - if no parameters given , takes the default value in the parameters.
say_hello()

#function should return something
def sum(num1,num2):
  return num1+num2

print(sum(10,5))