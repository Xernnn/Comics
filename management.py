import tkinter as tk
from tkinter import ttk
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

        # Create header_frame and details_frame
        self.header_frame = tk.Frame(
            self.window,
            bg="#1A1918"
        )
        self.details_frame = tk.Frame(
            self.window,
            bg="#1A1918"
        )
        self.header_frame.pack(side=tk.TOP, fill=tk.X)
        self.details_frame.pack(fill=tk.X, pady=0, padx=0)
        self.window.config(bg="#1A1918")

        # Create user_info and user_menu objects
        user_info = UserInfo(root)
        user_menu = UserMenu(root)

        # Create sidebar object
        self.sidebar = LeftMenu(root)
        self.left_menu = LeftMenu(self.details_frame)  # Create an instance of LeftMenu

        # Create the header object
        self.header = Header(self.header_frame, self.go_to_homepage, self.search_comic, self.sidebar.toggle_left_menu, user_menu, user_info)

        # Assign the callback function after creating header
        user_menu.update_user_icon_callback = self.header.update_user_icon

        # Pack header
        self.header.pack(side=tk.TOP, fill=tk.X)

        # Create the content
        content_frame = ttk.Frame(root, style='ContentFrame.TFrame')
        self.content = Content(content_frame, self.show_details)
        content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        

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
        results = self.header.search("All", search_query)
        self.content.search_and_update_content(results)

    def show_details(self, comic):
        from comics import ComicDetails
        ComicDetails(self.window, comic)
        
    def search_callback(self, search_query):
        results = self.header.search(1, search_query)
        self.content.search_and_update_content(results)
        


