import tkinter as tk

def say_hello():
    print("Hello!")

root = tk.Tk()
root.title("My Tkinter App")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

btn = tk.Button(root, text="Click me", command=say_hello)
btn.pack(pady=10)

root.mainloop()