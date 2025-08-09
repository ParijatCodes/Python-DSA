#create 3 classes which are inherited and add a method bark
class Animals:
    pass
class Pets(Animals):
    pass
class dog(Pets):
    @staticmethod
    def bark():
        print("Bhow! Bhow!! Bhowww!!!")
d= dog()

d.bark()