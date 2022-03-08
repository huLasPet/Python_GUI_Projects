# TODO: Count the number of characters typed in and how long it took.
#  When clicking start the type field should come to focus right away.
# Get the length of the text entry - len(text_entry.get()) - and use time to get the speed


import tkinter as tk
import requests


class TypingSpeed:
    def __init__(self):
        self.bs_text = ""
        self.displayed_text = ""

    def get_sample_text(self):
        response = requests.get(url="https://corporatebs-generator.sameerkumar.website/")
        self.bs_text = response.json()["phrase"]
        return self.bs_text

    def display_text_and_entry(self):
        self.displayed_text = typing.get_sample_text()
        text_display.config(text=self.displayed_text)
        text_entry.config(width=len(self.displayed_text))
        text_entry.grid(column=0, row=1, sticky="w")

    def start_typing(self):
        pass
        # start timer and focus on text input
        # enter should end the timing


typing = TypingSpeed()
window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Typing speed")

text_display = tk.Label(text="Press start")
text_display.grid(column=0, row=0, sticky="w")
text_entry = tk.Entry(window)

start_stop_button = tk.Button(text="Start", command=typing.display_text_and_entry)
start_stop_button.grid(column=0, row=2)

typing.get_sample_text()
window.mainloop()
