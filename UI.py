import tkinter as tk

def on_button_click():
    print("Button clicked!")

window = tk.Tk()
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()
window.mainloop()