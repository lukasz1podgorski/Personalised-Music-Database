import sqlite3
import time
from xlsxwriter.workbook import Workbook

conn = sqlite3.connect("new_spotify_releases.sqlite")
c = conn.cursor()

new_releases_data = [
    ("Miuosh", "Początek", "2023-09-22", "polish hip hop"),
    ("Doja Cat", "Scarlet", "2023-09-22", "dance pop"),
    ("Taco Hemingway", "1-800-OŚWIECENIE", "2023-09-21", "polish hip hop"),
]


def create_table():
    c.execute("CREATE TABLE new_releases(artist_name, release_name, release_date, artist_genre)")
    # conn.close()


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

    # conn.close()


def select_a_genre(genre):
    for row in c.execute('SELECT * FROM new_releases WHERE artist_genre '
                         'LIKE ? ORDER BY release_date', ('%' + genre + '%',)):
        print(row)

    # conn.close()


def write_to_xls():
    time_string = time.strftime("%Y%m%d-%H%M%S")
    workbook = Workbook(f'export_{time_string}.xlsx')
    worksheet = workbook.add_worksheet()
    column_names = ["Artist", "Album title", "Release date", "Genre"]
    for j, column_name in enumerate(column_names):
        worksheet.write(0, j, column_name)

    c.execute("SELECT * FROM new_releases")
    selection = c.execute("SELECT * FROM new_releases ")
    for i, row in enumerate(selection, start=1):
        for j, value in enumerate(row):
            worksheet.write(i, j, row[j])
    workbook.close()


def clear_the_table():
    c.execute('DELETE FROM new_releases')
    conn.commit()
    # conn.close()


def close_the_db():
    conn.close()
