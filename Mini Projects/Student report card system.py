# Student Report Card System

class student:

            
    def funct(self):
        self.roll_no=int(input("Enter roll no of student : "))
        self.name=input("Enter Student name : ")
        self.marks=list(map(int,input("Enter marks of students in 3 subjects : ").split()))        
        while len(self.marks)!=3:
            print("Enter marks in 3 sunjects ")
            self.marks=list(map(int,input("Enter marks of students in 3 subjects : ").split()))
    
    def avg_calc(self):
        print("----- student report -----")
        print("   --Name--",self.name)
        print("   --Roll_No--",self.roll_no)
        print(" --list of marks--",self.marks)
        sum=0
        for i in self.marks:
            sum+=i
        average=sum/3    
        print("  --average marks are--",average)
       
    def status(self):
        p=0
        for x in self.marks: 
            if x>=33: 
                p+=1
        if(p==3):
            print("Student Status : Pass ")
        else:
            print("Student Status : Fail ")
                
        
obj1=student()
obj1.funct()
obj1.avg_calc()
obj1.status()


        
                
        






    
