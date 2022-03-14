#TODO: Create a GUI app where if you stop typing for 5 seconds the text will disappear
#Try to check if the length of the entry changed and if not, delete what is there

import tkinter as tk
import time

window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Disappearing text")
text_display = tk.Text(window)
text_display.insert('end', "ASD")
text_display.grid(column=1, row=0)
print(text_display.get(1.0, 'end'))
window.mainloop()