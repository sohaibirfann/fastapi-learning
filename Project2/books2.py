from fastapi import FastAPI

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, "Computer Science", "CodeItOut", "Good book I Guess", 5),
    Book(2, "Be Fast with FastAPI", "CodeItOut", "Great book I Guess", 5),
    Book(3, "Master Endpoints", "CodeItOut", "Awesome book I Guess", 5),
    Book(4, "HP1", "Author 1", "Boilerplate Desc", 2),
    Book(5, "HP2", "Author 2", "Boilerplate Desc", 3),
    Book(6, "HP3", "Author 3", "Boilerplate Desc", 1),
]


@app.get("/books")
async def read_all_books():
    return BOOKS
