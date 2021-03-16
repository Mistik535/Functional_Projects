import tkinter as tk


def select_all():
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()


def switch_all():
    for check in [over_18, commercial, follow]:
        check.toggle()


def show():
    print("Флажок 18", over_18_value.get())
    print("Реклама", commercial_value.get())

win = tk.Tk()

over_18_value = tk.StringVar()
over_18_value.set("No")
commercial_value = tk.IntVar()
win.geometry(f"300x400+100+200")
win.title("Мое первое графическое приложение")

over_18 = tk.Checkbutton(win, text="Вам исполнилось 18 лет?",
                         variable=over_18_value,
                         offvalue="No",
                         onvalue="Yes"
                         )
commercial = tk.Checkbutton(win, text="Хотите получать рекламу?",
                            variable=commercial_value,
                         offvalue=0,
                         onvalue=1)
follow = tk.Checkbutton(win, text="Хотите подписаться на канал?")
over_18.pack()
commercial.pack()
follow.pack()
tk.Button(win, text="select_all", command=select_all).pack()
tk.Button(win, text="deselect_all", command=deselect_all).pack()
tk.Button(win, text="switch_all", command=switch_all).pack()
tk.Button(win, text="Show", command=show).pack()

win.mainloop()
