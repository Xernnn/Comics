import tkinter as tk
from PIL import Image, ImageTk
from header import Header
from content import Content
from left_menu import LeftMenu
from user_menu import UserMenu

class Management(Header, Content, LeftMenu, UserMenu):
    def __init__(self, root):
        self.window = root
        self.window.title("ComixHub Homepage")

        self.details_frame = tk.Frame(
            self.window,
            bg="#1A1918"
        )
        self.details_frame.pack(fill=tk.BOTH, expand=True)

        Header.__init__(self, self.go_to_homepage, self.search_comic)
        Content.__init__(self)
        LeftMenu.__init__(self)
        UserMenu.__init__(self)
    
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
