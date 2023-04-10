import tkinter as tk
from management import Management
import time


def show_loading_screen():
    loading_screen = tk.Toplevel(root)
    loading_screen.geometry('300x100')
    loading_screen.title('Loading...')

    loading_label = tk.Label(loading_screen, text='Loading comics, please wait...', font=('Comic Sans MS', 14))
    loading_label.pack(pady=20)

    root.update()
    return loading_screen


if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')

    # Hide the main window
    root.withdraw()

    # Show the loading screen
    loading_screen = show_loading_screen()

    # Load the comics
    obj = Management(root)

    # Destroy the loading screen after loading is complete
    loading_screen.destroy()

    # Show the main window
    root.deiconify()

    root.mainloop()
