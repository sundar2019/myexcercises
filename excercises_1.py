#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
#Hint: Use of print with end 

fill='*'
empty=' '
for image in picture:
  for pixel in image:
    if(pixel):
      print(fill, end='') # end appends the print statements
    else:
      print(empty, end='')
  print('') # need a new lin4


#Excercise2:
#Check for duplicates in this list

some_list=['a','b','c','b','d','m','n','n']

duplicates=[]
for item in some_list:
   num_list=some_list.count(item)
   if num_list>1:
      if item not in duplicates:
        duplicates.append(item)
print(duplicates)
  




