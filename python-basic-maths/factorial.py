class basic_maths:
    def __init__(self, number: int):
        self.number = number

    def factorial_of_n(self)-> int:
        fact = 1
        for i in range(self.number,1,-1):
            fact = fact * i
        return fact

    
fact = basic_maths(0)
print(fact.factorial_of_n())
        