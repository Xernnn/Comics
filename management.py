import tkinter as tk
from PIL import Image, ImageTk
from header import Header
from content import Content
from left_menu import LeftMenu
from user_menu import UserMenu
from user_info import UserInfo

class Management(Header, UserMenu):
    def __init__(self, root):
        self.window = root
        self.window.title("ComixHub Homepage")

        self.details_frame = tk.Frame(
            self.window,
            bg="#1A1918"
        )
        self.details_frame.pack(fill=tk.BOTH, expand=True)

        self.left_menu = LeftMenu(self.details_frame)  # Create an instance of LeftMenu

        user_menu = UserMenu(root)
        user_info = UserInfo(root)
        Header.__init__(self, self.go_to_homepage, self.search_comic, self.left_menu.toggle_left_menu, user_menu, user_info)
        
        self.content = Content(self.details_frame)  # Create an instance of Content and store it as an attribute
    
    def go_to_homepage(self):
        # Perform the action when the ComicHub label is clicked
        print("ComicHub label clicked")
        self.window.destroy()
        root = tk.Tk()
        root.state('zoomed')
        obj = Management(root)
        root.mainloop()
        
    def search_comic(self, search_query):
        print(f"Searching for: {search_query}")


