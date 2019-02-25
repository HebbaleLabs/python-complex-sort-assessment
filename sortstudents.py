from math import isclose

class Student:

  def __init__(self, sid, name, cgpa):
    self.sid = sid
    self.name = name
    self.cgpa = cgpa

  def __eq__(self, other):
    return self.sid == other.sid and self.name == other.name and isclose(self.cgpa, other.cgpa)

  def __hash__(self):
    return hash(self.sid)

  def __repr__(self):
    return "Student( %a, %a, %f )" % (self.sid ,self.name , self.cgpa)

  def __str__(self):
    return "An instance of Student: [ %a, %a, %f ]" % (self.sid ,self.name , self.cgpa)

def sort(studentlist):
  return None