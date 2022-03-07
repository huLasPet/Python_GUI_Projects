#TODO: Count the number of characters typed in and how long it took. When clicking start the type field should come to focus right away.

import tkinter as tk


window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Typing speed")

text_entry = tk.Entry(window)
text_entry.insert(index=0, string="Start typing")
text_entry.grid(column=0, row=0, sticky="w")

window.mainloop()