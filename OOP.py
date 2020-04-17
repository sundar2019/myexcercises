# OOP's concepts


class PlayerCharacter:
  def __init__(self,name,age):
    self.name=name
    self.age = age

player1 = PlayerCharacter("John",22)
player2 = PlayerCharacter("Jim",32)

print(player1.name)
print(player1.age)

print("Player {0} and age is {1}".format(player1.name,player1.age))
print("Player {0} and age is {1}".format(player2.name,player2.age))