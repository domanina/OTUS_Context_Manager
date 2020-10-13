import json
from csv import DictReader

#открытие файлов
with open("users.json", "r") as j:
    users = json.loads(j.read())

with open('books.csv') as f:
    reader = DictReader(f)
    books_list = list(reader)

#усечение ключей массива юзеров, добавление ключа книги
short_info_users = users
for row in short_info_users:
    for key in row.copy().keys():
        if (key != "name" and key != "gender" and key != "address"):
            del row[key]

for row in short_info_users:
    row["books"] = []

#усечение ключей массива книг
short_info_books = books_list
for row in short_info_books:
    for key in row.copy().keys():
        if (key != "Title" and key != "Author" and key != "Height"):
            del row[key]

# раздача книг юзерам
for row in short_info_users:
    for row_books in short_info_books:
        row["books"] = row_books


