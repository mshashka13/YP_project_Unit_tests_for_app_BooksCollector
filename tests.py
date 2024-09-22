from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_three_books(self):
        book = BooksCollector()
        book.add_new_book('Война миров')
        book.add_new_book('Зов Ктулху')
        book.add_new_book('Противостояние')
        assert len(book.books_genre) == 3

    def test_add_new_book_add_books_without_name(self):
        book = BooksCollector()
        book.add_new_book('')
        assert len(book.books_genre) == 0

    def test_add_new_book_add_book_again(self, create_new_book):
        create_new_book.add_new_book('Война миров')
        assert len(create_new_book.get_books_genre()) == 1

    def test_add_new_book_add_book_over_40_symbols(self):
        book = BooksCollector()
        book.add_new_book('романроманроманроманроманроманроманроманр')
        assert len(book.books_genre) == 0


    def test_set_book_genre_set_real_genre(self, create_new_book):
        create_new_book.set_book_genre('Война миров', 'Фантастика')
        assert create_new_book.get_book_genre('Война миров') == f'Фантастика'

    def test_set_book_genre_set_unreal_genre(self, create_new_book):
        create_new_book.set_book_genre('Война миров', 'Фэнтези')
        assert create_new_book.books_genre != {'Война миров': 'Фэнтези'}

    def test_set_book_genre_set_genre_without_book(self):
        book = BooksCollector()
        book.set_book_genre('Война миров', 'Фантастика')
        assert book.books_genre != {'Война миров': 'Фантастика'}


    def test_get_book_genre_book_without_genre(self, create_new_book):
        assert create_new_book.get_book_genre('Война миров') == f''


    def test_get_books_with_specific_genre_real_genre(self, create_new_books_with_genres):
        assert create_new_books_with_genres.get_books_with_specific_genre('Фантастика') == ['Война миров']

    def test_get_books_with_specific_genre_without_books(self, create_new_books_with_genres):
        assert create_new_books_with_genres.get_books_with_specific_genre('Детективы') == []


    def test_get_books_for_children_child_rating(self, create_new_books_with_genres):
        assert create_new_books_with_genres.get_books_for_children() == ['Война миров']

    def test_get_books_for_children_without_books(self):
        book = BooksCollector()
        book.add_new_book('Зов Ктулху')
        book.set_book_genre('Зов Ктулху', 'Ужасы')
        assert book.get_books_for_children() == []


    def test_add_book_in_favorites_real_book(self, create_new_book):
        create_new_book.add_book_in_favorites('Война миров')
        assert create_new_book.get_list_of_favorites_books() == ['Война миров']

    def test_add_book_in_favorites_add_book_again(self, create_new_book):
        create_new_book.add_book_in_favorites('Война миров')
        create_new_book.add_book_in_favorites('Война миров')
        assert create_new_book.favorites == ['Война миров']

    def test_add_book_in_favorites_unreal_book(self):
        book = BooksCollector()
        book.add_book_in_favorites('Противостояние')
        assert book.favorites == []


    def test_delete_book_from_favorites_real_book(self, create_new_book):
        create_new_book.add_book_in_favorites('Война миров')
        create_new_book.delete_book_from_favorites('Война миров')
        assert create_new_book.favorites == []

    def test_delete_book_from_favorites_unreal_book(self):
        book = BooksCollector()
        book.delete_book_from_favorites('Противостояние')
        assert book.favorites == []


    def test_get_list_of_favorites_books_empty_list(self, create_new_book):
        assert create_new_book.favorites == []

