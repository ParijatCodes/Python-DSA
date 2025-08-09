#get salary after incremnt and increment of a employee using class
class employee:
    salary= 90000
    increment= 5

    @property
    def newSalary(self):
        return self.salary + (self.salary * (self.increment/100))
    @newSalary.setter
    def newSalary(self,salary):
        self.increment= ((salary/self.salary)-1)*100

e= employee()
print(e.newSalary)
print(e.increment)