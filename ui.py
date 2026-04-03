import tkinter as tk
import tkinter.ttk as ttk
import main

def main_page():
    window = tk.Tk()
    button = tk.Button(text="Grab Stats")
    button.bind("<ButtonPress>", lambda e : main.main())
    button2 = ttk.Button(text="Themed button" )
    button.pack()
    button2.pack()
    window.mainloop()


main_page()
