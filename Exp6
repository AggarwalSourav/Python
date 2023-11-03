class student:
    def getstudent(self):
        self.__rollno=input("Enter Roll No. : ")
        self.__name=input("Enter the student name: ")
        self.__physicsMarks= int(input("Enter Physics Marks: "))
        self.__chemistryMarks=int(input("Enter Chemistry Marks:"))
        self.__mathMarks=int(input("Enter Maths marks: "))
    def putstudent(self):
        print(self.__rollno,self.__name,((self.__physicsMarks+self.__chemistryMarks+self.__mathMarks)/3))
    def Search(self,min,max):
        per=(self.__physicsMarks+self.__chemistryMarks+self.__mathMarks)/3
        if(per>=min and per<=max):
            return True
        else:
            return False
studentdict=dict()
n=int(input("How many students you want to input :"))
for i in range(n):
    s= student()
    rollno=s.getstudent()
    studentdict.setdefault(rollno,s)

rollno=input("Enter the roll no. you want to search : ")
s=studentdict.get(rollno,"Not Found!!")
if(isinstance(s,student)):
    s.putstudent()
else:
    print(s)

print("All studerts who scored more than 60 percentage are: ")
gradeAstudent=list(filter(lambda s:s.Search(60,100),studentdict.values()))
if(len(gradeAstudent)==0):
    print("Record Not Found!!")
else:
    for s in gradeAstudent:
        s.putstudent()
