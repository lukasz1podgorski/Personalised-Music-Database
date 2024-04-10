import sqlite3

conn = sqlite3.connect("new_spotify_releases.sqlite")
c = conn.cursor()

new_releases_data = [
    ("Miuosh", "Początek", "2023-09-22", "polish hip hop"),
    ("Doja Cat", "Scarlet", "2023-09-22", "dance pop"),
    ("Taco Hemingway", "1-800-OŚWIECENIE", "2023-09-21", "polish hip hop"),
]


def create_table():
    c.execute("CREATE TABLE new_releases(artist_name, release_name, release_date, artist_genre)")
    conn.close()


def insert_to_table(insert_data):
    c.executemany("INSERT INTO new_releases VALUES(?, ?, ?, ?)", insert_data)
    conn.commit()


def remove_duplicates_from_table():
    c.execute('DELETE FROM new_releases WHERE rowid NOT IN '
              '(SELECT min(rowid) FROM new_releases GROUP BY artist_name, release_name )')
    conn.commit()


def select_from_table():
    for row in c.execute('SELECT * FROM new_releases ORDER BY release_date'):
        print(row)

    conn.close()


def select_a_genre(genre):
    for row in c.execute('SELECT * FROM new_releases WHERE artist_genre '
                         'LIKE ? ORDER BY release_date', ('%'+genre+'%',)):
        print(row)

    conn.close()


def clear_the_table():
    c.execute('DELETE FROM new_releases')
    conn.commit()
    conn.close()
