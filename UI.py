import tkinter as tk

window = tk.Tk()
window.title("Simple GUI")
window.geometry("400x300")
def on_button_click():
    print("Button clicked!")
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=20)
label = tk.Label(window, text="Hello, Tkinter!")

label.pack(pady=10)
window.mainloop()