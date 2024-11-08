## __Unit тестирование для приложения BooksCollector__ 

___

### __Тесты (tests):__  

__1) Метод add_new_book:__
- test_add_new_book_add_three_books - добавление трех книг в словарь
- test_add_new_book_add_books_without_name - невозможность добавить книгу без названия
- test_add_new_book_add_book_again - невозможность добавить одну и ту же книгу повторно (проверяется метод get_books_genre)
- test_add_new_book_add_book_over_40_symbols - невозможность добавить книгу с названием длиннее 40 символов

__2) Метод set_book_genre:__
- test_set_book_genre_set_real_genre - добавление существующего жанра к существующей в словаре книге (проверяется метод get_book_genre)
- test_set_book_genre_set_unreal_genre - невозможность добавления несуществующего жанра к существующей в словаре книге
- test_set_book_genre_set_genre_without_book - невозможность добавления жанра к несуществующей в словаре книге

__3) Метод get_book_genre(позитивная проверка в методе 2):__
- test_get_book_genre_book_without_genre - невозможность получения жанра от книги с неуказанным жанром

__4) Метод get_books_with_specific_genre:__
- test_get_books_with_specific_genre_real_genre - выборка по жанру с добавленными книгами с существующим жанром
- test_get_books_with_specific_genre_without_books - невозможность выбрать книги по существующему жанру, если в нем отсутствуют книги

__5) Метод get_books_for_children:__
- test_get_books_for_children_child_rating - выборка книг по возрастному рейтингу
- test_get_books_for_children_without_books - невозможность выборки книг, если рейтинг не подходит для детей

__6) Метод add_book_in_favorites:__
- test_add_book_in_favorites_real_book - добавление существующей книги в избранное (проверяется метод get_list_of_favorites_books)
- test_add_book_in_favorites_add_book_again - невозможность добавить одну и ту же книгу в избранное повторно
- test_add_book_in_favorites_unreal_book - невозможность добавить несуществующую книгу в избранное

__7) Метод delete_book_from_favorites:__
- test_delete_book_from_favorites_real_book - удаление существующей в списке избранное книги из списка
- test_delete_book_from_favorites_unreal_book - невозможность удаления несуществующей в списке избранное книги из списка

__8) Метод get_list_of_favorites_books(позитивная проверка в методе 6):__
- test_get_list_of_favorites_books_empty_list - получение пустого списка избранное, если в нем отсутсвуют книги


  
