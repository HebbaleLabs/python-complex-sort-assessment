import unittest
from sortstudents import sort, Student
from parameterized import parameterized

class SortStudentsTest(unittest.TestCase):

  @parameterized.expand([
    ('students with unique cgpa',
     [
       Student(1, 'Fiza', 3.6),
       Student(2, 'Ayush', 4.6),
       Student(3, 'Roy', 3.7),
       Student(4, 'Ammarah', 4.2),
       Student(5, 'Reese', 4.1)
     ],
     [
       Student(2, 'Ayush', 4.6),
       Student(4, 'Ammarah', 4.2),
       Student(5, 'Reese', 4.1),
       Student(3, 'Roy', 3.7),
       Student(1, 'Fiza', 3.6)
     ]),

    ('students with unique cgpa',
     [
       Student(1, 'X', 3.85),
       Student(2, 'Y', 4.15),
       Student(3, 'Z', 3.75),
       Student(4, 'A', 4.25),
       Student(5, 'B', 4.55)
     ],

     [Student(5, 'B', 4.55),
      Student(4, 'A', 4.25),
      Student(2, 'Y', 4.15),
      Student(1, 'X', 3.85),
      Student(3, 'Z', 3.75)])
  ])
  def test_sort_cgpa(self, name, input_values, expected):
    self.longMessage = True
    actual = sort(input_values)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_values, expected, actual)
    try:
      self.assertListEqual(expected, actual, message)
    except AssertionError as e:
      e.args = (message,)
      raise

  @parameterized.expand([
    ('students with same cgpa different names',
     [
       Student(1, 'Fiza', 3.6),
       Student(2, 'Ayush', 4.6),
       Student(3, 'Roy', 3.6),
       Student(4, 'Ammarah', 4.2),
       Student(5, 'Reese', 4.1)
     ],
     [
       Student(2, 'Ayush', 4.6),
       Student(4, 'Ammarah', 4.2),
       Student(5, 'Reese', 4.1),
       Student(1, 'Fiza', 3.6),
       Student(3, 'Roy', 3.6)
     ]),
    ('students with same cgpa different names',
     [
       Student(1, 'P', 4.6),
       Student(2, 'Q', 4.1),
       Student(3, 'R', 4.6),
       Student(4, 'S', 4.2),
       Student(5, 'T', 3.8)
     ],
     [
       Student(1, 'P', 4.6),
       Student(3, 'R', 4.6),
       Student(4, 'S', 4.2),
       Student(2, 'Q', 4.1),
       Student(5, 'T', 3.8)]
     )
  ])
  def test_sort_cgpa_names(self, name, input_values, expected):
    self.longMessage = True
    actual = sort(input_values)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_values, expected, actual)
    try:
      self.assertListEqual(expected, actual, message)
    except AssertionError as e:
      e.args += (message,)
      raise

  @parameterized.expand([
    ('students with same cgpa and names',
     [
       Student(1, 'Roy', 3.6),
       Student(2, 'Ayush', 4.6),
       Student(3, 'Roy', 3.6),
       Student(4, 'Ammarah', 4.2),
       Student(5, 'Roy', 3.6)
     ],
     [
       Student(2, 'Ayush', 4.6),
       Student(4, 'Ammarah', 4.2),
       Student(1, 'Roy', 3.6),
       Student(3, 'Roy', 3.6),
       Student(5, 'Roy', 3.6)
     ]),
    ('students with same cgpa and names',
     [
       Student(1, 'A', 3.6),
       Student(2, 'B', 4.2),
       Student(3, 'C', 4.1),
       Student(4, 'A', 4.2),
       Student(5, 'B', 3.6)
     ],
     [
       Student(4, 'A', 4.2),
       Student(2, 'B', 4.2),
       Student(3, 'C', 4.1),
       Student(1, 'A', 3.6),
       Student(5, 'B', 3.6)
     ])
  ])
  def test_sort_ids(self, name, input_values, expected):
    self.longMessage = True
    actual = sort(input_values)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_values, expected, actual)
    try:
      self.assertListEqual(expected, actual, message)
    except AssertionError as e:
      e.args += (message,)
      raise
