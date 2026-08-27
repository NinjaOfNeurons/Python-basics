class GCD:
    def __init__(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2

    def gcd_from_list(self)->list:
        greater = max(self.num1,self.num2)
        while True:

            if(greater % self.num1 == 0 and  greater % self.num2 == 0):
                return greater
            
            greater += 1


obj_gcd = GCD(12,20)
print(obj_gcd.gcd_from_list())