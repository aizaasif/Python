class Student:
    record=[]
    def add_stu(self):
        self.name=input("Enter the name of the student : ")
        self.record.append(self.name)
        self.Roll_No=input("Enter the Roll_No of the student : ")
        self.record.append(self.Roll_No)
        self.marks=list(map(int,input("Enter marks of students in 3 subjects : ").split()))
        self.record.append(self.marks)
    
    def avg_calc(self):
        s=0
        for i in self.marks:
            s+=i
        self.avg=s/3
        return self.avg
    
    def grade(self):
        if(self.avg>=90):
            grade="A"
        elif(self.avg>=75 and self.avg<=89):
            grade="B"
        elif(self.avg>=60 and self.avg<=74):
            grade="C"
        elif(self.avg>=40 and self.avg<=59):
            grade="D"
        else:
            grade="F"
        return grade
    
    def data(self):
        print("Student Data")
        print("Name : ",self.name)
        print("Roll_No : ",self.Roll_No)
        print("Marks : ",self.marks)
        print("Average Marks : ",self.avg_calc())
        print("Grade : ",self.grade())
          
    def view_data(self):
        choice=input("Enter roll_no you want to search : ")
        if choice==self.Roll_No:
            obj1.data()
        else:
            print("Student dosent exsist ")

obj1=Student()
obj1.add_stu()
obj1.view_data()


