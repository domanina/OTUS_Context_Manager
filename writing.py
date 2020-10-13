from reading import *
import json


# запись в файл нового массива
with open("users_with_books.json", "w") as f:
    s = json.dumps(short_info_users, indent=4)
    f.write(s)