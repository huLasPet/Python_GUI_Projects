#TODO
#Create a gui that lets you select a picture, where you want to put the watermark, what text, what color it should be
#and where to save it


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import tkinter as tk
from tkinter import filedialog, colorchooser

image_source = "Select an image"
text_color = ""


def watermark(img, w_text):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./arial.ttf", 32)
    draw.text((0, 0), w_text, text_color[0], font=font)
    img.save('watermarked.jpg')
    w_done = tk.Label(text="Done")
    w_done.grid(column=0, row=3, sticky="w")


def get_file():
    global image_source
    file = filedialog.askopenfile(parent=window, mode='rb', title='Choose a file')
    if file:
        image_source = Image.open(file)
        image.config(text="Image selected", fg="green")


def get_color():
    global text_color
    text_color = colorchooser.askcolor()
    color.config(text="Color selected", fg=text_color[1])


window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Watermarking tool")

#Labels
image = tk.Label(text="Image:")
image.grid(column=0, row=0, sticky="w")
text_to_add = tk.Label(text="Text to add:")
text_to_add.grid(column=0, row=1, sticky="w")
color = tk.Label(text="Color:")
color.grid(column=0, row=2, sticky="w")

#Entries
text_to_add_entry = tk.Entry(width=20)
text_to_add_entry.insert(index=0, string="Enter the text")
text_to_add_entry.grid(column=1, row=1, sticky="w")

#Buttons
watermark_button = tk.Button(text="Watermark", width=20,
                                  command=lambda: watermark(image_source, text_to_add_entry.get()))
watermark_button.grid(column=1, row=3, sticky="w")
color_button = tk.Button(text="Browse color", width=20, command=get_color)
color_button.grid(column=1, row=2, sticky="w")
search_button = tk.Button(text="Browse file", width=20, command=get_file)
search_button.grid(column=1, row=0, sticky="w")


window.mainloop()