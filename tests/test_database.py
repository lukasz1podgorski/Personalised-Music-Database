import database as database
import unittest.mock as mock


@mock.patch("database.create_table")
def test_create_table(mock_create_table):
    mock_create_table.return_value = "CREATE TABLE new_releases(artist_name, release_name, release_date, artist_genre)"
    data = database.create_table()

    assert data == "CREATE TABLE new_releases(artist_name, release_name, release_date, artist_genre)"


@mock.patch("database.insert_to_table")
def test_insert_to_table(mock_insert_to_table):
    mock_insert_to_table.return_value = "INSERT INTO new_releases VALUES(?, ?, ?, ?)"
    db_data = []
    data = database.insert_to_table(db_data)

    assert data == "INSERT INTO new_releases VALUES(?, ?, ?, ?)"


@mock.patch("database.select_from_table")
def test_select_from_table(mock_select_from_table):
    mock_select_from_table.return_value = {"artist": "Ed Sheeran", "album_title": "Autumn Variations",
                                           "release_date": "2023-09-29", "genre": "pop, singer-songwriter pop, uk pop"}
    data = database.select_from_table()

    assert data == {"artist": "Ed Sheeran", "album_title": "Autumn Variations",
                    "release_date": "2023-09-29", "genre": "pop, singer-songwriter pop, uk pop"}


@mock.patch("database.select_a_genre")
def test_select_a_genre(mock_select_a_genre):
    mock_select_a_genre.return_value = {"artist": "Ed Sheeran", "album_title": "Autumn Variations",
                                        "release_date": "2023-09-29", "genre": "pop, singer-songwriter pop, uk pop"}
    data = database.select_a_genre('pop')

    assert data == {"artist": "Ed Sheeran", "album_title": "Autumn Variations",
                    "release_date": "2023-09-29", "genre": "pop, singer-songwriter pop, uk pop"}
