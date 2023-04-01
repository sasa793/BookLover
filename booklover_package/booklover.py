import numpy as np
import pandas as pd
    
class BookLover:
    """This is a class that contains methods and information about a specific  person's books. Whether it's their favorite, the number read, the name, or rating, etc."""
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, book_rating):
        """This function tries to add book name and rating to the dataframe created. It also checkes whether the book is already in the book list and it it's not it gets added in along with it's associated rating"""
        self.book_name = str(book_name)
        self.rating = int(book_rating)
        if self.book_name in self.book_list['book_name'].values:
            print("This book already exists in your created book list")
        else:
            if (self.rating > 5) | (self.rating < 0):
                  print("The rating must be between 0 and 5, try again!")
            else:
                new_book = pd.DataFrame({
                    'book_name': [book_name],
                    'book_rating': [book_rating]
                })
                self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
                self.num_books +=1

    def has_read(self, book_name):
        """This function takes the book name and determines if the person has read that book."""
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
        
    def num_books_read(self):
        """This function just returns the total number of books the person has read."""
        self.num_books = len(self.book_list['book_name'])
        return self.num_books
    
    def fav_books(self):
        """This function returns the peron's favorite books, those of which have a rating greater than 3."""
        return self.book_list[self.book_list['book_rating'] > 3]