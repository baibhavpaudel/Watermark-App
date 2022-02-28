from tkinter import *

# TODO: Create a sample GUI window and set up UI
window = Tk()
window.title("Watermark Your Images")
window.minsize(width=900, height=600)
window.config(padx=20, pady=30)

label = Label(window, text='Put a custom Watermark\n on your pictures!',
              font=("Courier", 35, "bold"), bg='green', padx=20, pady=20)
label.pack(padx=50, pady=50, side='top')

frame = Frame(window, width=600, height=200, bg='red', highlightbackground='yellow', highlightthickness=10,
              padx=20, pady=20)
frame.pack(padx=50, pady=50, side='bottom')
frame.pack_propagate(False)

upload_btn = Button(frame, text='Upload Image File', padx=10, pady=10, bg='grey',
                    font=('Arial', 10))
upload_btn.pack(padx=125, pady=50)


#TODO: Upload an image file using the GUI window


#TODO: Use Pillow to edit the image and add a watermark

window.mainloop()