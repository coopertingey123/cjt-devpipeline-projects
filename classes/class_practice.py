class Animal:
  def __init__(self, name, color, number_of_legs):
    self.name = name
    self.color = color
    self.number_of_legs = number_of_legs
  
  def make_sound(self):
    print("Generic Animals make no sound")
   
  def print_me(self):
    print(f'name: {self.name}')
    print(f'color: {self.color}')
    print(f'legs: {self.number_of_legs}')
    # print(self.type)

class Cat(Animal):
  def __init__(self, color):
    Animal.__init__(self, 'Cat', color, 4)
  
  def make_sound(self):
    print("Meow!!!")

class Dog(Animal):
  def __init__(self, color):
    Animal.__init__(self, 'Dog', color, 4)
  
  def make_sound(self):
    print("Woof!! Woof!!")
  
class Bird(Animal):
  def __init__(self,color):
    Animal.__init__(self, 'Bird', color, 2)
  
  def make_sound(self):
    print("Tweet, tweet!")



stupid_cat = Cat("black")

stupid_cat.print_me()
stupid_cat.make_sound()
print(stupid_cat.color)

cool_dog = Dog("golden")

cool_dog.print_me()
cool_dog.make_sound()
print(cool_dog.color)