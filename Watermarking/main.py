#TODO
#Create a gui that lets you select a picture, where you want to put the watermark, what text, what color it should be
#and where to save it


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import tkinter
from tkinter import filedialog

image_source = ""


def watermark(img, w_text):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./arial.ttf", 32)
    draw.text((0, 0), w_text, (0, 0, 0), font=font)
    img.save('watermarked.jpg')


def get_file():
    global image_source
    file = filedialog.askopenfile(parent=window,mode='rb',title='Choose a file')
    if file:
        image_source = Image.open(file)


window = tkinter.Tk()
window.config(padx=20, pady=20)
window.title("Watermarking tool")
canvas_widget = tkinter.Canvas(width=200, height=200, highlightthickness=0)
# logo_img = tkinter.PhotoImage(file="logo.png")
# canvas_widget.create_image(100, 100, image=logo_img)
canvas_widget.grid(column=1, row=0, sticky="w")

#Labels
image = tkinter.Label(text="Image:")
image.grid(column=0, row=1, sticky="w")
text_to_add = tkinter.Label(text="Text to add:")
text_to_add.grid(column=0, row=2, sticky="w")
color =tkinter.Label(text="Color:")
color.grid(column=0, row=3, sticky="w")

#Entries
image_entry = tkinter.Entry(width=32)
image_entry.grid(column=1, row=1, sticky="w")
image_entry.focus()
text_to_add_entry = tkinter.Entry(width=45)
text_to_add_entry.insert(0, "Test")
text_to_add_entry.grid(column=1, row=2, columnspan=2, sticky="w")
color_entry = tkinter.Entry(width=32)
color_entry.grid(column=1, row=3, sticky="w")

#Buttons
watermark_button = tkinter.Button(text="Watermark", width=38,
                                  command=lambda: watermark(image_source, text_to_add_entry.get()))
generate_button = tkinter.Button(text="Browse color", width=9)
watermark_button.grid(column=1, row=4, columnspan=2, sticky="w")
generate_button.grid(column=2, row=3, sticky="w")
search_button = tkinter.Button(text="Browse file", width=9, command=get_file)
search_button.grid(column=2, row=1, sticky="w")




window.mainloop()