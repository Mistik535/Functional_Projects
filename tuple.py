import tkinter as tk

def say_hello():
    print("hello")

def add_label():
    label= tk.Label(win, text= "new")
    label.pack()

def counter():
    global count
    count+=1
    btn4["text"]= f"count: {count}"

count=0

win = tk.Tk()

btn1=tk.Button(win, text="Hello",
               command=say_hello)

btn2=tk.Button(win, text="add new label",
               command=add_label)

btn3=tk.Button(win, text="add new label lambda",
               command=lambda: tk.Label(win, text= "new lambda").pack())

btn4=tk.Button(win, text=f"count: {count} ",
               command=counter,
               activebackground="blue",
               bg="red",
               state=tk.DISABLED
               )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

photo =tk.PhotoImage(file="fun.png")
win.iconphoto(False, photo)
win.config(bg="#2DFF00")
win.title("Battlefield")
win.geometry("500x600+100+200")
win.minsize(300,400)
win.maxsize(700,800)
win.resizable(True, True)
label_1 = tk.Label(win, text="""Hello!
world""",
                   bg="red",
                   fg="white",
                   font=("Arial", 20, "bold"),
                   padx = 20,
                   pady = 40,
                   width = 20,
                   height = 10,
                   anchor="ne",
                   relief=tk.RIDGE,
                   bd=10,
                   justify=tk.RIGHT
                   )
label_1.pack()


win.mainloop()
