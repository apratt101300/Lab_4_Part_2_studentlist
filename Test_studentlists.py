'''
Practice using
 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn
'''

from studentlists import ClassList, StudentError
from unittest import TestCase
import unittest

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Maria')
        test_class.remove_student('Maria')
        self.assertNotIn('Maria', test_class.class_list)


    def test_max_students_less_than_or_equal_zero(self):
        with self.assertRaises(StudentError): # test a class with zero students allowed
            ClassList(0)
        with self.assertRaises(StudentError): # test a class with negative students allowed
            ClassList(-5)

            
    def test_max_students_greater_than_zero(self):
        ClassList(1) # make sure no error is raised when creating a max size greater than zero


    def test_remove_student_not_in_list(self): # test StudentError is raised when removing a student not in the classlist
        test_class = ClassList(5)
        test_class.add_student('Maria')
        test_class.add_student('Thomas')
        test_class.add_student('Eric')

        with self.assertRaises(StudentError): 
            test_class.remove_student('Monica')
        

    def test_remove_student_from_empty_list(self): # test student error is raised when removing a student from an empty list
        test_class = ClassList(1)

        with self.assertRaises(StudentError): 
            test_class.remove_student('Monica')


    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    # test that is_enrolled returns false if the specified student isn't in the class list
    def test_student_not_enrolled(self): 
        test_class = ClassList(5)       
        test_class.add_student('Anna')
        test_class.add_student('Mario')
        test_class.add_student('Roger')

        self.assertFalse(test_class.is_enrolled('Erica'))


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


  
    ## TODO write a test for index_of_student when the class_list list is empty.  
    # Assert index_of_student returns None for a student if the list is empty. 
    # use assertIsNone.
 
 
    ## TODO write another test for index_of_student. In the case when the 
    # class_list is not empty but has some students.
    # assert that searching for a student name that is not in the list, returns None.

   
    # Test to see if the is_class_full method returns True when the class is full
    def test_full_class_list(self):
        test_class = ClassList(5)       
        test_class.add_student('Anna')
        test_class.add_student('Mario')
        test_class.add_student('Roger')
        test_class.add_student('Alyssa')
        test_class.add_student('Renee')
        self.assertTrue(test_class.is_class_full())


    def test_class_empty_or_not_full(self):
        test_class = ClassList(2) # test is_class_full on empty classlist
        self.assertFalse(test_class.is_class_full())

        test_class.add_student('Maria') # test is_class_full on not full classlist
        self.assertFalse(test_class.is_class_full())
        


if __name__ == '__main__':
    unittest.main()