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
  #
  # IMPORTANT:
  # 1. Write your solution in this function
  # 2. Do not make changes to the function signature
  # 3. Use the 'pip-install' command in the IDE, to install any requirements. This takes a few seconds.
  # 4. Use the 'run' command in the IDE, to run the main method. You can also invoke the main method from the terminal.
  # 5. Use the 'run-tests' command in the IDE, to run unit tests. The 'pip-install' command must be run before this.
  return None

def main():
  example_list_of_students = [ Student(sid = 1, name= 'A', cgpa = 2.5), Student(sid = 2, name = 'B', cgpa= 3.5)]
  sorted_students = sort(example_list_of_students)
  print('Sorted list: {0}\n'.format(sorted_students))

if __name__ == '__main__':
  main()