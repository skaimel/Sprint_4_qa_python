import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize("name", [
        "1984",
        "Преступление и наказание",
        "Оно",
        "Властелин колец",
        "Гарри Поттер и философский камень"
    ])
    def test_add_new_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize("name, genre", [
        ("1984", "Фантастика"),
        ("Преступление и наказание", "Детективы"),
        ("Оно", "Ужасы"),
        ("Властелин колец", "Фэнтези"),
        ("Гарри Поттер и философский камень", "Фэнтези")
    ])
    def test_get_books_with_specific_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_with_genre = collector.get_books_with_specific_genre(genre)
        assert name in books_with_genre

    @pytest.mark.parametrize("name, genre", [
        ("1984", "Фантастика"),
        ("Преступление и наказание", "Детективы"),
        ("Оно", "Ужасы"),
        ("Властелин колец", "Фэнтези"),
        ("Гарри Поттер и философский камень", "Фэнтези")
    ])
    def test_no_books_with_unused_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_with_genre = collector.get_books_with_specific_genre("Приключения")
        assert books_with_genre == []

    @pytest.mark.parametrize("name, genre", [
        ("1984", "Фантастика"),
        ("Преступление и наказание", "Детективы"),
        ("Оно", "Ужасы"),
        ("Властелин колец", "Фэнтези"),
        ("Гарри Поттер и философский камень", "Фэнтези")
    ])
    def test_get_book_genre_dict(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert isinstance(collector.get_books_genre(), dict)

    @pytest.mark.parametrize("name, genre", [
        ("1984", "Фантастика"),
        ("Преступление и наказание", "Детективы"),
        ("Оно", "Ужасы"),
        ("Властелин колец", "Фэнтези"),
        ("Гарри Поттер и философский камень", "Фэнтези")
    ])
    def test_no_age_restricted_books_for_kids(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_for_children = collector.get_books_for_children()
        assert name not in books_for_children

    @pytest.mark.parametrize("name", [
        "1984",
        "Преступление и наказание",
        "Оно",
        "Властелин колец",
        "Гарри Поттер и философский камень"
    ])
    def test_add_book_to_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    def test_add_non_dict_book_to_favorites_not_added(self):
        collector = BooksCollector()
        name = "Приключения принца"
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_twice_without_delete(self):
        collector = BooksCollector()
        name = "1984"
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books().count(name) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        name = "Преступление и наказание"
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

