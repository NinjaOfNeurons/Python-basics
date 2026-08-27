class GCD:
    def __init__(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2

    def gcd_from_list(self)->list:
        gcd_num = []
        mul =1
        for i in range(2,min(self.num1,self.num2) + 1):
            if(self.num1 % i == 0   and   self.num2 % i == 0):
                gcd_num.append(i)  
       
        for i in gcd_num:
            mul = mul * i
        return mul 


obj_gcd = GCD(12,20)
print(obj_gcd.gcd_from_list())