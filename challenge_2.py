class calculator:
    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def addition(self):
        print("Addition of no1 & no2 : ",self.no1 + self.no2)

    def substraction(self):
        print("substraction of no1 & no2 : ",self.no1 - self.no2)
    
    def multiplication(self):
        print("multiplication of no1 & no2 : ",self.no1 * self.no2)

    def division(self):
        print("division of no1 & no2 : ",self.no1 / self.no2)


cal_obj = calculator(int(input("Enter no1 : ")),int(input("Enter no1 : ")))
cal_obj.addition()
cal_obj.substraction()
cal_obj.multiplication()
cal_obj.division()
    
