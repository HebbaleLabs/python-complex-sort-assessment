import unittest
from sortstudents import sort, Student


class SortStudentsTest(unittest.TestCase):

  def test_sort_cgpa(self):
    studentcollection = [Student(1, 'Fiza', 3.6),
                         Student(2, 'Ayush', 4.6),
                         Student(3, 'Roy', 3.7),
                         Student(4, 'Ammarah', 4.2),
                         Student(5, 'Reese', 4.1)]
    sortedcollection = sort(studentcollection)
    expectedcollection = [Student(2, 'Ayush', 4.6),
                          Student(4, 'Ammarah', 4.2),
                          Student(5, 'Reese', 4.1),
                          Student(3, 'Roy', 3.7),
                          Student(1, 'Fiza', 3.6)]
    self.assertListEqual(expectedcollection, sortedcollection)

  def test_sort_cgpa_names(self):
    studentcollection = [Student(1, 'Fiza', 3.6),
                         Student(2, 'Ayush', 4.6),
                         Student(3, 'Roy', 3.6),
                         Student(4, 'Ammarah', 4.2),
                         Student(5, 'Reese', 4.1)]
    sortedcollection = sort(studentcollection)
    expectedcollection = [Student(2, 'Ayush', 4.6),
                          Student(4, 'Ammarah', 4.2),
                          Student(5, 'Reese', 4.1),
                          Student(1, 'Fiza', 3.6),
                          Student(3, 'Roy', 3.6)]
    self.assertListEqual(expectedcollection, sortedcollection)

  def test_sort_cgpa_names_ids(self):
    studentcollection = [Student(1, 'Roy', 3.6),
                         Student(2, 'Ayush', 4.6),
                         Student(3, 'Roy', 3.6),
                         Student(4, 'Ammarah', 4.2),
                         Student(5, 'Roy', 3.6)]

    sortedcollection = sort(studentcollection)
    expectedcollection = [Student(2, 'Ayush', 4.6),
                          Student(4, 'Ammarah', 4.2),
                          Student(1, 'Roy', 3.6),
                          Student(3, 'Roy', 3.6),
                          Student(5, 'Roy', 3.6),]
    self.assertListEqual(expectedcollection, sortedcollection)
