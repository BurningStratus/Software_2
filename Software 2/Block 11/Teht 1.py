
class Publication:
    def __init__(self, name):
        self.name = name

    
class Book(Publication):
    def  __init__(self, name, writer, pages):
        super().__init__(name)
        self.writer = writer
        self.pages = pages
    
    def info(self):
        return f"{self.name} was written by {self.writer}. It has {self.pages} pages."
    
class Paper(Publication):
    def __init__(self, name, redactor):
        Publication.__init__(self, name)
        self.redactor = redactor
    
    def info(self):
        return f"{self.name} was redacted by {self.redactor}"

book_0 = Paper("Aku Ankka", "Aki Hyyppä")
book_1 = Book("Hytti n6","Roosa Liksom", 200)

print(book_0.info())
print(book_1.info())
