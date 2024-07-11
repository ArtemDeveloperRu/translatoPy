from googletrans import Translator
from tkinter import *
from tkinter import messagebox
from settings import *

# Create window
windows = Tk()
windows.title(nameApp)
windows.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

# Create object
canvas = Canvas(windows, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
canvas.pack()

text = Label(canvas, text="Enter the text you want to translate: ")
text.place(relx=0.5, rely=0.1, anchor=CENTER)

text_entry = Entry()
text_entry.place(relx=0.5, rely=0.2, width=200, anchor=CENTER)

language_label = Label(canvas, text="Enter the target language: ")
language_label.place(relx=0.5, rely=0.3, anchor=CENTER)

language_entry = Entry()
language_entry.place(relx=0.5, rely=0.4, width=200, anchor=CENTER)

def translate_text():
    tr = Translator()
    try:
        target_language = language_entry.get()
        text_translation = tr.translate(text_entry.get(), dest=target_language).text
        messagebox.showinfo("Translation", text_translation)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

translate_button = Button(canvas, text="Translate", command=translate_text)
translate_button.place(relx=0.5, rely=0.8, width=200, anchor=CENTER)

# Set window to non-resizable
windows.resizable(False, False)
windows.mainloop()