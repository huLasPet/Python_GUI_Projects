#TODO: Create a GUI app where if you stop typing for 5 seconds the text will disappear
#Try to check if the length of the entry changed and if not, delete what is there

import tkinter as tk


class TextDelete:
    def __init__(self):
        self.char_count = 0
        self.prev_count = 0

    def delete(self):
        self.prev_count = self.char_count
        self.char_count = len(text_display.get(1.0, 'end'))
        if self.prev_count == self.char_count:
            text_display.delete(1.0, 'end')
        window.after(5000, self.delete)


delete_class = TextDelete()
window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Disappearing text")
text_display = tk.Text(window)
text_display.insert('end', "Stop typing for 5 seconds and lose what you have typed")
text_display.grid(column=0, row=0)
delete_class.delete()
window.mainloop()
