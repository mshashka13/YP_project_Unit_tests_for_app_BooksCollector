import pytest

from main import BooksCollector


@pytest.fixture
def create_new_book():
    book = BooksCollector()
    book.add_new_book('Война миров')
    return book


@pytest.fixture
def create_new_books_with_genres():
    book = BooksCollector()
    book.add_new_book('Война миров')
    book.set_book_genre('Война миров', 'Фантастика')
    book.add_new_book('Зов Ктулху')
    book.set_book_genre('Зов Ктулху', 'Ужасы')
    return book
