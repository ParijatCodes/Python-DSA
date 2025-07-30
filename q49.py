#just a class functioon
class Programmer:
    company= "Microsoft"
    def __init__(self, name, salary, lang):
        self.name= name
        self.salary= salary
        self.lang= lang

p= Programmer("Parijat", "1Lakh", "Python")
print(f"Name:{p.name}\nSalary:{p.salary}\nLang:{p.lang}\nCompany:{p.company}")