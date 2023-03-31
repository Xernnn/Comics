import tkinter as tk

class UserMenu:
    def __init__(self):
        pass

    def show_user_menu(self, event):
        self.user_menu_window = tk.Toplevel(self.window)
        self.user_menu_window.title("User Menu")
        self.user_menu_window.geometry("300x200")

        username_label = tk.Label(self.user_menu_window, text="Username:")
        username_label.pack(pady=(10, 0))

        self.username_entry = tk.Entry(self.user_menu_window)
        self.username_entry.pack(pady=(5, 10))

        password_label = tk.Label(self.user_menu_window, text="Password:")
        password_label.pack(pady=(0, 0))

        self.password_entry = tk.Entry(self.user_menu_window, show="*")
        self.password_entry.pack(pady=(5, 10))

        self.forget_password_button = tk.Button(
            self.user_menu_window,
            text="Forget Password",
            command=self.forget_password
        )
        self.forget_password_button.pack(pady=(0, 10))

        self.register_button = tk.Button(
            self.user_menu_window,
            text="Register",
            command=self.register
        )
        self.register_button.pack(pady=(0, 0))
    
    def login(self):
        print("Login")

    def signup(self):
        print("Sign up")

    def sidebar_action(self, button_text):
        print(f"Clicked {button_text}")
        
    def forget_password(self):
        print("Forget password")

    def register(self):
        print("Register")