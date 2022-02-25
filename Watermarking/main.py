#TODO
#Create a gui that lets you select a picture, where you want to put the watermark, what text, what color it should be
#and where to save it


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import tkinter


def watermark(img, w_text):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./arial.ttf", 32)
    draw.text((0, 0), w_text, (0, 0, 0), font=font)
    img.save('watermarked.jpg')


image_source = Image.open("img.jpg")
watermark_text = "TEST"
watermark(image_source, watermark_text)

window = tkinter.Tk()
window.config(padx=20, pady=20)
window.title("Watermarking tool")
canvas_widget = tkinter.Canvas(width=200, height=200, highlightthickness=0)
# logo_img = tkinter.PhotoImage(file="logo.png")
# canvas_widget.create_image(100, 100, image=logo_img)
canvas_widget.grid(column=1, row=0, sticky="w")

#Labels
website = tkinter.Label(text="Image:")
website.grid(column=0, row=1, sticky="w")
username = tkinter.Label(text="Text to add:")
username.grid(column=0, row=2, sticky="w")
password =tkinter.Label(text="Color:")
password.grid(column=0, row=3, sticky="w")

#Entries
website_entry = tkinter.Entry(width=32)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()
username_entry = tkinter.Entry(width=45)
username_entry.insert(0, "default@random.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
password_entry = tkinter.Entry(width=32)
password_entry.grid(column=1, row=3, sticky="w")

#Buttons
add_button = tkinter.Button(text="Add", width=38,) #command=)
generate_button = tkinter.Button(text="Browse", width=9,) #command=)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")
generate_button.grid(column=2, row=3, sticky="w")
search_button = tkinter.Button(text="Browse", width=9,) #command=)
search_button.grid(column=2, row=1, sticky="w")




window.mainloop()