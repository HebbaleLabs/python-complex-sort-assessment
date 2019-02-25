from operator import attrgetter

class Student:

  def __init__(self, sid, name, cgpa):
    self.sid = sid
    self.name = name
    self.cgpa = cgpa

  def __repr__(self):
    return "Student( %a, %a, %f )" % (self.sid ,self.name , self.cgpa)

  def __str__(self):
    return "An instance of Student: [ %a, %a, %f ]" % (self.sid ,self.name , self.cgpa)

def sort(studentlist):
  return None