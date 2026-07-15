#magic methods are just functions that start with __ and end with __ like the popular __init__
#they are found within classes
class Book :
    def __init__(self,title,author,pages):#init is like saying in it like book as title pages author in it
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return f'I am {self.author} i published the book {self.title} and it was {self.pages} pages'
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return self.pages<other.pages
    def __gt__(self, other):
        return self.pages>other.pages
    def __add__(self, other):
        return self.pages +other.pages
    def __contains__(self, item):
        return item in self.title or item in self.author
    def __getitem__(self, key):
        if key== 'title':
            return self.title
        if key == 'author':
            return self.author
book1=Book('Hobbit','J.R.R.Token',310)
book2=Book('Harry Potter and the philsopher stone','J.K.Rowling',223)
book3=Book('The lion,he witch and the wardrobe','C.S.Lewis',172)
book4=Book('The lion,he witch and the wardrobe','C.S.Lewis',282)
print(book2)#this is possible because of __str__ it means return this string of text when asked to print the object
print (book3==book4)#this works because of the function __eq__ (meaning EQual to)
print(book1<book3)#this works because of the function __lt__ (meaning Less Than)
print(book1>book3)#this works because of the function __gt__ (meaning Greater Than)
print(book1+book3)#this works because of the function __add__ (meaning ADDition)
print('wa' in book3)#this works because of the function __contains__ this is extremely convient to find out if a work or sentence in a object
print(book1.title)
print(book1['title'])#this works because of the function __getitem__ which seems soo gimmickey cause the same results will come out if u serch for it directly unless is not in the list