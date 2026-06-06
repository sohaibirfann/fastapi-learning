from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "Math"},
    {"title": "Title Four", "author": "Author Four", "category": "Math"},
    {"title": "Title Five", "author": "Author Two", "category": "Science"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.get("/books/{dynamic_param}")
# async def read_dynamic(dynamic_param: str):
#     return {"dynamic_param": dynamic_param}


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


# query param version
@app.get("/books/author_books/")
async def get_author_book_by_query(author_name: str):
    author_books = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get("author").casefold() == author_name.casefold():
            author_books.append(BOOKS[i])

    return author_books


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{book_author}/")
async def read_authot_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)

    return books_to_return


@app.post("/books/{create_book}")
async def add_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/{update_book}")
async def book_update(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def remove_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


# path param version
@app.get("/books/author_books/{author_name}")
async def get_author_of_books(author_name: str):
    author_books = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get("author").casefold() == author_name.casefold():
            author_books.append(BOOKS[i])

    return author_books
