import tkinter as tk
from management import Management

if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
    obj = Management(root)
    root.mainloop()
