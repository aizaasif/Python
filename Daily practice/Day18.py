class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks       


    def cal_avg(self):
        sam=0
        for i in self.marks:
            sam+=i
        print(sam/3)


s1=student("Aiza",[100,90,80])
s1.cal_avg()

class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def cal_avg(self):
        a=0
        sam=0
        for i in self.price:
            sam+=i
        print(f"Average price is {a} product is",sam/3)
        a+=1
        
p1=product("Bread",[100,110,120])
p1.cal_avg()
p2=product("eggs",[10,20,30])
p2.cal_avg()