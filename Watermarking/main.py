from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import tkinter as tk
from tkinter import filedialog, colorchooser

variables = {"image_source": "Select an image", "text_color": "", "corner": []}
dropdown_choices = ["Top Left", "Top Right", "Bottom Left", "Bottom Right"]


def watermark(img, w_text):
    """Adds the watermark to the picture.
    It needs the picture and the text to be provided when calling it."""
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./arial.ttf", 32)
    draw.text(variables["corner"], w_text, variables["text_color"][0], font=font)
    img.save('watermarked.jpg')
    w_done = tk.Label(text="Done")
    w_done.grid(column=0, row=4, sticky="w")


def get_file():
    """Opens a file browser to select the picture to be watermarked."""
    file = filedialog.askopenfile(parent=window, mode='rb', title='Choose a file')
    if file:
        variables["image_source"] = Image.open(file)
        image.config(text="Image selected", fg="green")


def get_color():
    """Opens a color picker for the text to be added."""
    variables["text_color"] = colorchooser.askcolor()
    color.config(text="Color selected", fg=variables["text_color"][1])


def change_dropdown(*args):
    """Dropdown menu to select the location of the text.
    Used with tk.OptionMenu.trace()"""
    selected = dropdown.get()
    match selected:
        case "Top Left":
            variables["corner"] = [0, 0]
        case "Bottom Left":
            variables["corner"] = [0, variables["image_source"].size[1] - 30]
        case "Top Right":
            variables["corner"] = [variables["image_source"].size[0] - (len(text_to_add_entry.get()) * 14), 0]
        case "Bottom Right":
            variables["corner"] = [variables["image_source"].size[0] - (len(text_to_add_entry.get()) * 14),
                                   variables["image_source"].size[1] - 30]


window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Watermarking tool")
dropdown = tk.StringVar(window)
dropdown.set("Top Left")

# Labels
image = tk.Label(text="Image:")
image.grid(column=0, row=0, sticky="w")
text_to_add = tk.Label(text="Text to add:")
text_to_add.grid(column=0, row=1, sticky="w")
color = tk.Label(text="Color:")
color.grid(column=0, row=2, sticky="w")
dropdown_label = tk.Label(text="Select a corner")
dropdown_label.grid(column=0, row=3)

# Entries
text_to_add_entry = tk.Entry(width=20)
text_to_add_entry.insert(index=0, string="Enter the text")
text_to_add_entry.grid(column=1, row=1, sticky="w")

# Buttons
watermark_button = tk.Button(text="Watermark", width=20,
                             command=lambda: watermark(variables["image_source"], text_to_add_entry.get()))
watermark_button.grid(column=1, row=4, sticky="w")
color_button = tk.Button(text="Browse color", width=20, command=get_color)
color_button.grid(column=1, row=2, sticky="w")
search_button = tk.Button(text="Browse file", width=20, command=get_file)
search_button.grid(column=1, row=0, sticky="w")
dropdown_menu = tk.OptionMenu(window, dropdown, *dropdown_choices)
dropdown_menu.grid(column=1, row=3)
dropdown.trace('w', change_dropdown)

window.mainloop()
