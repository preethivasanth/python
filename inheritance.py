class student:
 def inputdata(self):
  self.name=(input("enter the student name"))
  self.mark=(input("enter the mark"))
 def display(self):
  print("student name is",self.name)
  print("student mark is",self.mark)
class sports(student):
 game="athlete"
 rank=20
 def play(self):
  print("play the game",self.game)
  print("rank",self.rank)
s=sports()
s.display()
s.play()
