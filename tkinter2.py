import tkinter as tk


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print("empty entry")

def delete_entry():
    name.delete(0, tk.END)

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title("new tkinter application")
tk.Label(win,text= "Имя").grid(row=0,column=0,stick="w")
name = tk.Entry(win)
name.grid(row=0,column=1)
# for i in range(5):
#     for j in range (2):
#         tk.Button(win,text=f"Hello {i} {j}").grid(row=i, column=j, stick="we")

tk.Button(win,text="get",command=get_entry).grid(row=1, column=0, stick="we")
tk.Button(win,text="delete",command=delete_entry).grid(row=1, column=1, stick="we")
tk.Button(win,text="insert",command=lambda : name.insert(0, "hello"))\
    .grid(row=1, column=2, stick="we")


win.grid_columnconfigure(0,minsize=100)
win.grid_columnconfigure(1,minsize=100)

win.mainloop()
