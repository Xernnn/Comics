import tkinter as tk
from sort import SortSubMenu
from modify import ModifySubMenu

class LeftMenu:
    def __init__(self, details_frame, update_sort,  master=None, content=None):
        self.update_sort = update_sort
        self.master = master
        self.content = content
        self.details_frame = details_frame
        self.menu_visible = False
        self.left_menu_frame = tk.Frame(
            self.details_frame,
            bg="#1A1918",
            relief=tk.GROOVE
        )  # Initialize the left_menu_frame attribute
        self.create_left_menu()
    
    def toggle_left_menu(self, event):
        if self.menu_visible:
            self.hide_left_menu()
        else:
            self.left_menu_frame.place(x=0, y=66, width=250, height=1000)
            self.left_menu_frame.lift()
        self.menu_visible = not self.menu_visible

    def hide_left_menu(self):
        self.left_menu_frame.place_forget()

    def create_left_menu(self):
        self.create_button_frame(x=0, y=66, width=250, height=1000)
        self.hide_left_menu()

    def create_button_frame(self, x, y, width, height):
        button_frame = tk.Frame(
            self.details_frame,
            bg="#1A1918",
            relief=tk.GROOVE
        )
        button_frame.place(x=x, y=y, width=width, height=height)

        button_width = 24  # Adjust the desired button width
        button_height = 2  # Adjust the desired button height
        button_font = ("Arial", 12)  # Adjust the desired button font size
        button_padding = (5, 5)  # Adjust the desired padding between buttons
        
        submenu_classes = {
            "Sort": SortSubMenu,
            "Modify": ModifySubMenu
        }
        
        submenus = {}
        for index, (main_label, submenu_class) in enumerate(submenu_classes.items()):
            # action_callback = self.sort_callback()
            submenu = submenu_class(button_frame, self.content, index, button_width, button_height, button_font, button_padding, self.update_sort)
            submenus[main_label] = submenu

        self.submenus = submenus
        self.left_menu_frame = button_frame  # Assign the button_frame to self.left_menu_frame
        
        return button_frame
