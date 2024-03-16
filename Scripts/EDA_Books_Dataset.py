#!/usr/bin/env python
# coding: utf-8

# In[71]:


import json

import numpy as np
import pandas as pd

books = pd.read_csv("Books.csv", sep=";")
ratings = pd.read_csv("Ratings.csv", sep=";")
users = pd.read_csv("Users.csv", sep=";")
genres = pd.read_json("goodreads_book_genres_initial.json", lines=True)

# df = pd.read_json('goodreads_books.json', lines=True, chunksize = 10000)
# book_ids = pd.DataFrame()

# i = 0

# for chunk in df:
#     book_ids = pd.concat([book_ids, chunk[['book_id','isbn']]])
#     i += 1
#     print(i)

genres = genres.merge(
    book_ids[["book_id", "isbn"]],
    left_on="book_id",
    right_on="book_id",
    suffixes=(False, True),
)
books = genres.merge(books, left_on="isbn", right_on="ISBN")
books = books[
    ["book_id", "ISBN", "genres", "Title", "Author", "Year", "Publisher"]
].rename(columns={"book_id": "Book_Id", "genres": "Genres"})

display(genres)
display(books)
display(ratings)
display(users)


# In[72]:


# print("Genres")
# display(genres)
# genres.info()

print("Books")
display(books)
books.info()

print("Ratings")
display(ratings)
ratings.info()

print("Users")
display(users)
users.info()


# In[67]:


# Out of the 1,149,780 ratings, we have Books in our Books table for 739,447 of those ratings.
books_with_ratings = books.merge(ratings, left_on="ISBN", right_on="ISBN")
display(books_with_ratings)

# 111,314 (all but 359) Books in our Books table have at least one rating
distinct_books_rated = len(pd.unique(books_with_ratings["ISBN"]))
distinct_books_rated
