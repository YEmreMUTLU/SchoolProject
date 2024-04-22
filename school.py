import random
class school:
    def __init__(self,name):
        self.name=name

    class student:
        def __init__(self,name,surname,number,diciplinePoint,className,lessons={"Math":0,"English":0}):
            self.name=name
            self.surname=surname
            self.number=number
            self.diciplinePoint=diciplinePoint
            self.className=className
            self.lessons=lessons
        def dicipline(self):
            dicipline=input("Student Went A principle?(Please write yes or no!!: )")
            if dicipline=="yes":
                self.diciplinePoint-=10
                if self.diciplinePoint<=0:
                    print("The student is not a student anymore in this school")
                    self.name=None
                    self.surname=None
                    self.number=None
                    self.diciplinePoint=None
                    self.className=None
                else:
                    print("The student's dicipline point (-10 points) : ",self.diciplinePoint)
            elif dicipline!="yes" or dicipline=="no":
                print("Do not busy !")
        def show(self):
            print("""
                  // Student Info's//
            Name: {}
            Surname: {}
            Number: {}
            ClassName: {}
            Dicipline Point: {}

""".format(self.name,self.surname,self.number,self.className,self.diciplinePoint))
        def changeNotes(self):
            results=input("Please choose the lesson that you want to change the note ('Math' or 'English') :")
            if results=="Math":
                self.lessons["Math"]=int(input("Please write new note : "))
                if 0<=self.lessons["Math"]<=100:
                    print("You add the note successfully. New Math Note:",self.lessons["Math"])
                else:
                    print("You can't change the note!! ")
                    self.lessons["Math"]=0
            elif results=="English":
                    self.lessons["English"]=int(input("Please write new note : "))
                    if 0<=self.lessons["English"]<=100:
                        print("You add the note successfully. New English Note:",self.lessons["English"])
                    else:
                         print("You can't change the note!! ")
                         self.lessons["English"]=0
            else:
                print("There is not a lesson ")
        def showNotes(self):
            print("""
            // Your Notes
            Math Note: {}
            English Note: {}
""".format(self.lessons["Math"],self.lessons["English"]))
        def Teacher(self):
            num=random.randint(1,2)
            if num==1:
                print("Busted")     
                self.diciplinePoint-=2
            if num==2:
                print("Wrong Alert!")
class teachers:
    def __init__(self,name,surname,password=123456):
        self.name=name
        self.surname=surname
        self.password=password
    def teacherInfo(self):
        print("""
            //Teacher's Infos 
              Name: {}
              Surname: {}
              

""".format(self.name,self.surname,))