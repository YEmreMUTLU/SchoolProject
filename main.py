import school

Student1=school.school.student("Emre","Mutlu",1317,100,"7-A")
Teacher=school.teachers("Melissa","Blank",13579)
School=school.school("Stanley High School")

while True:
    print("""
          Dear Everyone Wellcome To {}  
""".format(School.name))
    print("""
    // Choose your Status
          [1] Student
          [2] Teacher
          [*] Quit
""")
    op=(input("Please Choose : "))
    if op=="1":
        print("""Student Database
                [1] Notes
                [2] Student Info
              """)

        op2=input("Please Choose : ")
        if op2=="1":
                if Student1.diciplinePoint==None:
                      pass
                else:
                 Student1.showNotes()
        elif op2=="2":
                Student1.show()
        else:
                print("Wrong paramatre . We informed the teacher")
                Student1.Teacher()

    elif op=="2":
           print("You are in Teacher's Database")
           print("""
            The List of Achievement
                     [1] Dicipline
                     [2] Student's Notes
                     [3] Teacher's Infos
""")
           op3=input("Choose One: ")
           if op3=="1":
                password=int(input("Please enter your teacher password: "))
                if password==Teacher.password:
                      Student1.dicipline()
                elif password!=Teacher.password:
                      print("Wrong Password! We informed ")
                      Student1.Teacher()
           elif op3=="2":
                  password=int(input("Please enter your teacher password: "))
                  if password==Teacher.password:
                        if Student1.diciplinePoint==None:
                              pass
                        else:
                         Student1.changeNotes()
                         Student1.showNotes()
                  elif password!=Teacher.password:
                      print("Wrong Password! We informed ")
                      Student1.Teacher() 
           elif op3=="3":
                 Teacher.teacherInfo()            
    elif op=="*":
          print("You are leaving the system. Have a good day")
          break
          

