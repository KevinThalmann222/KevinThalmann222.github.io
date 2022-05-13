import requests

book_information = requests.get(
    "https://openlibrary.org/api/books?bibkeys=ISBN:0201558025,LCCN:93005405&format=json"
)

for book_id in book_information.json():
    if (thumbnail_url := book_id['thumbnail_url']):
        print(f'Here is the thumbnail: {thumbnail_url}')