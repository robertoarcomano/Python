#!/usr/bin/python
class Record:
    name = ""
    def __init__(self,name):
        self.name = name

class Article(Record):
    price = 0
    def __init__(self,name,price):
        super().__init__(name)
        self.price = price

user = Record("John")
article = Article("laptop",1000)

print(f"user: {user.name} ")
print(f"article: {article.name} {article.price}")
