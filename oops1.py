OOps:



class Person:
  def __init__(self):

    self.name = "navya"
    self.gender = "female"
    self.age = 24

  def talk(self):
      print("hi i'm",self.name)
  def vote(self):
      if self.age<18:
          print("i'm not eligible")
      else:
          print("i'm eligible")
obj = Person()
Person.talk(obj)
Person.vote(obj)

O/p:
hi i'm navya
i'm eligible
Ex2:
    
class Person:
  def __init__(self,n,g,a):

    self.name = n
    self.gender = g
    self.age = a

  def talk(self):
      print("hi i'm",self.name)
  def vote(self):
      if self.age<18:
          print("i'm not eligible")
      else:
          print("i'm eligible")
obj1= Person("navya","female",24)
obj2= Person("mahesh","male",16)
obj1.talk()
obj1.vote()
obj2.talk()
obj2.vote()

O/p:
hi i'm navya
i'm eligible
hi i'm mahesh
i'm not eligible