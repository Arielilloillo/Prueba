class Person:
    name=""
    gender=""

class Student(Person):
    color=""
    calification=""

    def __init__(self,name,color,gender):
        self.name=name
        self.color=color
        self.gender=gender

class Teacher(Person):

    students=[Student("Rorro Pirroro", "normal","male"), Student("Zafiro","black","female)
    def evaluate(self,student):
        for i in self.students:
            if i.name==student:
                calification=input("What calification deserves?: ")
                i.calification=calification

class Library():
    books=["Baldor", "Lord of the rings", "Bible"]

    def delete_book(self):
        delete=input("Which book do you want?: ").title
        self.books.remove(delete)

    def add_book(self):
        add=input("What book do you want to add?: ").title
        self.books.append(add)
        
class Interface:

    library=Library()
    students=[Student("Rorro Pirroro", "normal","male"), Student("Zafiro","black","female"), Student("Ariel","black","male"),Student("Daniela","normal","female")]
    teacher=Teacher()

    def show_interface(self):
        decision=input("Select your rol: 1)Teacher. 2)Student.  ")
        if decision=="1":
            self.run_teacher()
        elif decision=="2":
            self.run_student()
        else:
                print("Invalid option.")

    def run_student(self):
        repeat=True
        while repeat:
            option=input("Select action: 1)Study. 2)Get drunk. 3)Get book. 4)Add book. 5)Salir.  ")
            if option=="1":
                print("I'm studing.")
            elif option=="2":
                print("Pist and then exist.")
            elif option=="3":
                self.library.add_book()
            elif option=="4":
                self.library.delete_book()
            elif option=="5":
                repeat=False
            else:
                print("Invalid option.")
    
    def run_teacher(self):
        repeat=True
        while repeat:
            option=input("Select action: 1)Teach. 2)Evaluate. 3)Salir.  ")
            if option=="1":
                print("Teaching in classroom.")
            elif option=="2":
                evaluate=input("Select student:").title
                self.teacher.evaluate(evaluate)
            elif option=="3":
                repeat=False
            else:
                print("Invalid option.")