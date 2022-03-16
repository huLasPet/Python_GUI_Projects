import tkinter as tk


class TextDelete:
    def __init__(self):
        self.text = ""
        self.prev_text = ""

    def delete(self):
        self.prev_text = self.text
        self.text = text_display.get(1.0, 'end')
        if self.prev_text == self.text:
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
