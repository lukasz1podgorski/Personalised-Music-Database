from callAPI import *
from database import *

# Get the list of new releases from Spotify API, assign genre to release
# and write results into SQLite database to create a personal music checklist.

# request access token for Spotify API
token = get_token()

# search for new releases music in certain country
new_releases = search_for_new_releases(token, "PL")

# list to insert to db
db_data = []

for count, release in enumerate(new_releases):
    # get release specific details
    release_item = new_releases[count]
    release_name = release_item["name"]
    release_type = release_item["type"]
    release_date = release_item["release_date"]
    # gather generic artist information
    artist_name = release_item["artists"][0]["name"]
    artist_id = release_item["artists"][0]["id"]
    # obtain artist genre
    artist_information = search_for_artist_info(token, artist_id)
    artist_genre = artist_information["genres"]

    # check if genre is NULL, if yes assign "not available"
    if len(artist_genre) > 0:
        artist_genre = str(artist_genre)
        artist_genre_str = artist_genre.translate({ord(i): None for i in '[\']'})
    else:
        artist_genre_str = "not available"

    print(str(count + 1) + ". " + artist_name + " - " + release_name + ", "
          + release_type + " released on: " + release_date + ", Genre: "
          + artist_genre_str)
    # append data to list of tuples in case user wants to save the list of new releases
    db_data.append((artist_name, release_name, release_date, artist_genre_str))

insert_to_db_bool = input("Do you want to add new releases to your personal database? (Y/N)")

if insert_to_db_bool == 'Y':
    insert_to_table(db_data)
    # make sure there will be no duplicated records in the table
    remove_duplicates_from_table()
    print("Please find the database entries below:")
    select_from_table()
elif insert_to_db_bool == "N":
    db_data.clear()
else:
    print("Please answer with Y or N.")
