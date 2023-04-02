import mysql.connector as sql
db = sql.connect(host="localhost",user="root",password="root",database="comics",port=3306,autocommit=True)
cursor = db.cursor(buffered=True)
if db.is_connected():
    print("db is connected")

# Input comic data
def comic_input():
    global title, comic_data 
    title = input(str("title: "))
    author = input(str("author: "))
    artist = input(str("artist: "))
    publisher = input(str("publisher: "))
    public_date = input(str("publisher_date: "))
    genre = input(str("genre: "))
    issue_number = input(str("issue_number: "))
    series = input(str("series: "))
    cover_image = input(str("cover_image: "))
    language = input(str("language: "))
    synopsis = input(str("synopsis: "))
    comic_data = (title, author, artist, publisher, public_date, genre, 
        issue_number, series, cover_image, language, synopsis)

# ADD comic
def add(comic_data):
    cursor.execute("""INSERT INTO comics(
        title, author, artist, publisher, public_date, genre, 
        issue_number, series, cover_image, language, synopsis) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",comic_data)
    
# DELETE comic
def delete(title):
    del_title = (title,)
    cursor.execute("DELETE FROM comics WHERE title=%s",del_title)
    
# UPDATE comic
def update(where, comic_data):
    temp_list = list(comic_data)
    temp_list.append(where)
    comic_data = tuple(temp_list)
    cursor.execute("""UPDATE comics
        SET title=%s, author=%s, artist=%s, publisher=%s, public_date=%s, genre=%s, 
        issue_number=%s, series=%s, cover_image=%s, language=%s, synopsis=%s 
        WHERE title=%s """,comic_data)

# # SEARCH comic
# def search(option, where):
#     where = (where,)
#     match option:
#         case 1:
#             cursor.execute("SELECT * from comics WHERE title = %s", where)
#         case 2:
#             cursor.execute("SELECT * from comics WHERE author = %s", where)
#         case 3:
#             cursor.execute("SELECT * from comics WHERE artist = %s", where)
#         case 4:
#             cursor.execute("SELECT * from comics WHERE language = %s", where)    

# MAIN FUNCTION
while 1:
    # print("1 to add comic, 2 to delete comic, 3 to update comic: ")
    choice = int(input("1 to add comic, 2 to delete comic, 3 to update comic, 4 to search: "))
    if choice == 1:
        comic_input()
        add(comic_data)
        print("comic",title,"has been added")

    if choice == 2:
        title = input(str("title: "))
        delete(title)
        print("comic",title,"has been deleted")
    if choice == 3:
        where= input(str("where: "))
        print("New: ")
        comic_input()
        update(where, comic_data)
        print("comic",where,"has been updated")
    # if choice == 4:
        # option = int(input("1 to search by title, 2 by author, 3 by artist, 4 by language: "))
        # where = input(str("where: "))
        # search(option, where)
        # result = cursor.fetchall()
        # for i in result:
        #     print(i)