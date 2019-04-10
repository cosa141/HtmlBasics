class Dog():
    #class object attributes go here
    species='Mammal'
    def __init__(self,breed='Mutt',name='Pup'):
        self.breed=breed
        self.name=name
# mydog=Dog(name='Airi')
# otherDog=Dog(breed='Border Collie')
# print(mydog.name)
# print(otherDog.breed)
# print(mydog.species)
print('Class Dog() can be used to create an instance of a dog with methods breed,name and species')
class Circle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    def area(self):
        return self.radius*self.radius * Circle.pi
    def set_radius(self,new_radius):
        self.radius=new_radius
print("The Circle() class can be used to return the area of a Circle with methods radius and new_radius")
# myc=Circle(3)
# print(myc.area())
# myc.set_radius(100)
# print(myc.area())

#INHERITANCE
class Animal():
    """docstring for Animal."""
    def __init__(self):
        print("Animal Created")
    def whoAmI(self):
        print('Animal')
    def eat(self):
        print('Eating')
class Dog(Animal):
    """docstring for Dog."""
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')
    def bark(self):
        print('WOOF')

class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return 'Title: {}, Author: {}, Pages: {}'.format(self.title,self.author,self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print('a book has been destroyed!!!')
b = Book('Python','Yang',200)
print(b)
