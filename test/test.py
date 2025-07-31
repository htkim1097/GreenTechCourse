import tkinter as tk

string = "여기에 입력하세요"

def on_entry_click(event):

    if entry.get() == string:
        entry.delete(0, tk.END)

def on_focusout(event):
    if entry.get() == "":
        entry.insert(0, string)


root = tk.Tk()
root.title("Entry Widget with Hint")

entry = tk.Entry(root)
entry.pack()
entry.insert(0, string)

entry.bind("<Button-1>", on_entry_click)
entry.bind("<FocusOut>", on_focusout)

entry1 = tk.Entry(root)
entry1.pack()

root.mainloop()