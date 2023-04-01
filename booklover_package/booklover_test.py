import numpy as np
import pandas as pd
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        Rose = BookLover("Rose", "RoseTulip@gmail.com", "nonfiction")
        Rose.add_book('Harry Potter', 4)
        testValue = 'Harry Potter' in Rose.book_list['book_name'].values
        message = "List does not contain this book"
        self.assertTrue(testValue, message)

        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        Rose = BookLover("Rose", "RoseTulip@gmail.com", "nonfiction")
        Rose.add_book('Harry Potter', 4)
        Rose.add_book('Harry Potter', 4)
        actual = 1
        expected = len(Rose.book_list[Rose.book_list['book_name'] == "Harry Potter"])
        self.assertEqual(expected, actual)
    
    
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        Patrick = BookLover("Patrick", "PatrickStar@gmail.com", "Mystery")
        Patrick.add_book('The Girl with the Dragon Tattoo', 4)
        testValue = Patrick.has_read('The Girl with the Dragon Tattoo')
        message = "Test value is not true."
        self.assertTrue(testValue, message)
        

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        Patrick = BookLover("Patrick", "PatrickStar@gmail.com", "Mystery")
        testValue = Patrick.has_read('Gone Girl') 
        message = "Test value is not true."
        self.assertFalse(testValue, message)
        

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        Sarah = BookLover("Sarah", "sarah101bb@gmail.com", "scifi")
        Sarah.add_book('Nineteen Eighty-Four', 5)
        Sarah.add_book('The Sirens of Titan', 2)
        Sarah.add_book('Dune', 4)
        Sarah.add_book('When Worlds Collide', 1)
        expected = 4
        actual = Sarah.num_books_read()
        self.assertEqual(expected, actual) 
        

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        Jackie = BookLover ("Jackie", "jackiestack@gmail.com", "Fiction")
        Jackie.add_book('The Great Gatsby', 4)
        Jackie.add_book('Moby Dick', 2)
        Jackie.add_book('Wonder', 3)
        Jackie.add_book('Chime', 5)
        actual = Jackie.fav_books()
        for i in actual.book_rating.values.tolist():
            if i > 3:
                return True
            else:
                return Error

        
if __name__ == '__main__':

    unittest.main(verbosity=3)
    
    
