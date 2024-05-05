class Animal:
    def eat(self):
        print("I am eating")
class dog(Animal):
    def eat(self):
        print("i am fucking hard")
        super().eat()
        print("iam fucking tooo hard")
prathamesh = dog()
prathamesh.eat()