class solution:
    def __init__(self, number):
        self.number = number

    def isprime(self)-> bool:
        for i in range(2,self.number):
            print(i)
            if self.number % i == 0:
                return(False)
            else:
                return(True)
        

prime = solution(2)
print(prime.isprime())