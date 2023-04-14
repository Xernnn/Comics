import mysql.connector as sql
db = sql.connect(host="localhost",user="root",password="root",database="comics",port=3306,autocommit=True)
cursor = db.cursor(buffered=True)
# if db.is_connected():
#     print("db is connected")

# ADD user
def add(user_data):
    values = tuple(user_data.values())
    cursor.execute("INSERT INTO users(username, password, avatar, gmail, role) VALUES(%s,%s,'https://imgur.com/a/OFOZMdx',%s,'user')",values)
# DELETE user
def delete(username):
    del_username = (username,)
    cursor.execute("DELETE FROM users WHERE username=%s",del_username)

# LOGIN user
def login(username, password):
    data = (username, password)
    cursor.execute("SELECT * from users WHERE username = %s and password = %s", data)

# UPDATE user
def update(gmail, username, avatar, where):
    data = (username, avatar, gmail, where)
    cursor.execute("UPDATE users SET username=%s, avatar=%s, gmail=%s WHERE username=%s",data)

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



# MAIN FUNCTION
""" 
while 1:
    choice = int(input("1 to register, 2 to login, 3 if u forgor password: "))
    if choice == 1:
        gmail = input(str("gmail: "))
        username = input(str("username: "))
        password = input(str("password: "))
        password_2 = input(str("confirm password: "))
        if password_2 == password:
            user_data = (username, password, gmail)
            add(user_data)
            print("registration complete")
        else: print("Please enter the same password")
    if choice == 2:
        username = input(str("username: "))
        password = input(str("password: "))
        login(username, password)
        result = cursor.fetchall()
        if len(result) == 0:
            print("username or password is invalid")
        else:
            print("login successfully")
            while 1:
                option = int(input("1 to update account, 2 to change password, 3 to delete account, 4 to logout: "))
                if option == 1:
                    where = username
                    gmail = input(str("gmail: "))
                    username = input(str("username: "))
                    avatar = input(str("link to your new avatar image: "))
                    update(gmail, username, avatar, where)
                    print("account updated\n")
                if option == 2:
                    where = username
                    old_password = input(str("enter old password: "))
                    if old_password == password:
                        password = input(str("enter new password: "))
                        password_2 = input(str("confirm password: "))
                        if password_2 == password:
                            changepw(password, where)
                            print("password changed\n")
                if option == 3:
                    if result[0][4] == 'admin':
                        where = input(str("user to delete: "))
                        conf = input(str("type YES to confirm: "))
                        if conf == "YES":
                            delete(where)
                            print("account",where,"has been deleted")
                        else: print("delete canceled")
                    else:
                        conf = input(str("type YES to confirm: "))
                        if conf == "YES":
                            delete(username)
                            print("your account has been deleted")
                            break
                        else: print("delete canceled") 
                if option == 4:
                    print("logout successfully")
                    break
    if choice == 3:
        gmail = input(str("gmail: "))
        username = input(str("username: "))
        forgor(gmail, username)
        result = cursor.fetchall()
        if len(result) == 0:
            print("gmail or username is invalid")
        else:
            print("your password is: ", result[0][1]) 
"""