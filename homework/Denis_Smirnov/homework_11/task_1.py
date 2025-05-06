class Book:
    material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        book_info = (
            f"Название: {self.title}, "
            f"Автор: {self.author}, "
            f"Страниц: {self.pages}, "
            f"Материал: {self.material}"
        )
        if self.reserved:
            return book_info + ", зарезервирована"
        else:
            return book_info


book1 = Book("Идиот", "Достоевский", 500, "12345")
book2 = Book("Преступление и наказание", "Достоевский", 600, "123456")
book3 = Book("Война и мир", "Толстой", 1200, "123457")
book4 = Book("Мастер и Маргарита", "Булгаков", 400, "1234567")
book5 = Book("Гарри Поттер", "Роулинг", 350, "12345324", reserved=True)

books = [book1, book2, book3, book4, book5]

for book in books:
    print(book)


class SchoolBook(Book):
    def __init__(self, title, author, pages, isbn, subject,
                 school_class, exercises, reserved=False):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.exercises = exercises

    def __str__(self):
        base = (f"Название: {self.title}, Автор: {self.author},"
                f" Страниц: {self.pages}")
        school_info = f", предмет: {self.subject}, класс: {self.school_class}"
        if self.reserved:
            school_info += ", зарезервирована"
        return base + school_info


school_book1 = SchoolBook(
    title="Математика",
    author="Иванов",
    pages=200,
    isbn="15325235",
    subject="Математика",
    school_class=9,
    exercises=True
)

school_book2 = SchoolBook(
    title="История России",
    author="Петров",
    pages=250,
    isbn="122353532",
    subject="История",
    school_class=8,
    exercises=True,
    reserved=True
)

school_books = [school_book1, school_book2]

for book in school_books:
    print(book)
