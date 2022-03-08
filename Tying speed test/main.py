import tkinter as tk
import requests
import time


class TypingSpeed:
    def __init__(self):
        self.bs_text = ""
        self.displayed_text = ""
        self.typed_chars = 0
        self.start = 0
        self.stop = 0

    def get_sample_text(self):
        response = requests.get(url="https://corporatebs-generator.sameerkumar.website/")
        self.bs_text = response.json()["phrase"]
        return self.bs_text

    def display_text_and_entry(self):
        if self.start == 0:
            self.start = time.time()
        self.typed_chars += len(text_entry.get())
        text_entry.delete(0, "end")
        text_entry.focus()
        self.displayed_text = self.get_sample_text()
        text_display.config(text=self.displayed_text)
        text_entry.config(width=len(self.displayed_text))
        text_entry.grid(column=1, row=1, sticky="w")

    def stop_typing(self):
        self.stop = time.time()
        self.typed_chars += len(text_entry.get())
        time_diff = self.stop - self.start
        text_display.config(text=f"Typed in {self.typed_chars} characters in {time_diff:.2} seconds.\n"
                                 f"This means your typing speed is {(self.typed_chars / time_diff):.2} chars a second.")


typing = TypingSpeed()
window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Typing speed")
window.bind('<Return>', lambda event: typing.display_text_and_entry())
window.bind('<Escape>', lambda event: typing.stop_typing())

text_display = tk.Label(text="Press Start or Enter to start\n"
                             "Get new text by pressing either\n"
                             "To finish press ESC")
text_display.grid(column=1, row=0)
text_entry = tk.Entry(window)


start_button = tk.Button(text="Start", command=typing.display_text_and_entry)
start_button.grid(column=0, row=2, sticky="w")

window.mainloop()
