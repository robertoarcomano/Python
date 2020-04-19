#!/usr/bin/python
class Record:
    name = ""

    def __init__(self, name):
        self.name = name


class Article(Record):
    price = 0

    def __init__(self, name, price):
        super().__init__(name)
        self.price = price


user = Record("John")
article = Article("laptop", 1000)

print("user: " + str({user.name}))
print("article: " + str({article.name}) + " " + str({article.price}))
