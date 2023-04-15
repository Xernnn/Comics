import mysql.connector as sql
db = sql.connect(host="localhost",user="root",password="root",database="comics",port=3306,autocommit=True)
cursor = db.cursor(buffered=True)
# if db.is_connected():
#     print("db is connected")

# ADD user
def add(user_data):
    values = tuple(user_data.values())
    cursor.execute("INSERT INTO users(username, password, avatar, gmail, role) VALUES(%s,%s,'https://i.imgur.com/HZ86ajE.png',%s,'User')",values)
# DELETE user
def delete(username):
    del_username = (username,)
    cursor.execute("DELETE FROM users WHERE username=%s",del_username)

# LOGIN user
def login(username, password):
    data = (username, password)
    cursor.execute("SELECT * from users WHERE username = %s and password = %s", data)

# UPDATE user
def update(age, favorite, avatar, username, where):
    data = (age, favorite, avatar, username, where)
    cursor.execute("UPDATE users SET age=%s, favorite=%s, avatar=%s WHERE username=%s",data)

# FORGOR PASSWORD
def forgot(gmail, username):
    data = (username, gmail)
    cursor.execute("SELECT password from users WHERE username = %s and gmail = %s", data)
    password = cursor.fetchone()
    if password:
        return password[0]
    else:
        return None

# CHANGE PASSWORD
def changepw(password, where):
    data = (password, where)
    cursor.execute("UPDATE users SET password=%s WHERE username=%s",data)
