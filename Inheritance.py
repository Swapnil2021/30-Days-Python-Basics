class Animal :
    name = ""
    def eat(self):
        print("I can eat")
class dog(Animal):
    def display(self):
        print("Myname is ",self.name)
labrador = dog()
labrador.name = "Rohu"
labrador.eat()
labrador.display()