class Dog:
  def __init__(self, breed, age, name, owner):
    self.breed = breed
    self.age = age
    self.name = name
    self.owner = owner
    
  def __str__(self):
    print("A " +str(self.age)+ "-year-old " +str(self.breed)+ " called " +str(self.name)+ " owned by " +str(self.owner))

  def change_owner(self, new_owner):
    self.owner = new_owner
    
  def get_older(self):
    self.age = int(self.age) + 1
    
if __name__ == '__main__':
    dog1 = Dog('Scottish Terrier', '1', 'Buster', 'Frederick')
    dog2 = Dog('Mixed-Breed', '5', 'Timmy', 'George')
    
    print(dog1)
    print(dog2)
    
    dog2.get_older()
    dog1.change_owner('Elizabeth')
    
    print(dog1)
    print(dog2)