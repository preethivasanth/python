class student:
 def __init__(self,name,mark):
    self.name=name
    self.mark=mark
 def inputdata(self):
    self.name=(input("enter the student name"))
    self.mark=(input("enter the mark"))
 def display(self):
    print("student name is",self.name)
    print("student mark is",self.mark)
stu=student("sam",80)
stu.display()
