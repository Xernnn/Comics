import tkinter as tk
from management import Management
import time
import mysql.connector as sql

def show_loading_screen():
    loading_screen = tk.Toplevel(root)
    loading_screen.geometry('300x100')
    loading_screen.title('Loading...')

    loading_label = tk.Label(loading_screen, text='Loading comics, please wait...', font=('Comic Sans MS', 14))
    loading_label.pack(pady=20)

    root.update()
    return loading_screen

if __name__ == "__main__":
    # Establish a connection to your database (replace the placeholders with your own values)
    cnx = sql.connect(host="localhost", user="root", password="root", database="comics", port=3306, autocommit=True)

    # Create a cursor object
    cursor = cnx.cursor()

    root = tk.Tk()
    root.state('zoomed')

    # Hide the main window
    root.withdraw()

    # Show the loading screen
    loading_screen = show_loading_screen()

    # Load the comics
    obj = Management(root, cursor)

    # Destroy the loading screen after loading is complete
    loading_screen.destroy()

    # Show the main window
    root.deiconify()

    root.mainloop()

    # Close the database connection
    cnx.close()
