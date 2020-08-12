import tkinter


def km_mile():
    # print(float(e1_value.get()))
    miles = float(e1_value.get())*1.6
    t1.insert(tkinter.END, miles)


top = tkinter.Tk()
b1 = tkinter.Button(top, text="convert", command=km_mile)
b1.grid(row=0, column=0)
e1_value = tkinter.StringVar()
e1 = tkinter.Entry(top, textvariable=e1_value)
e1.grid(row=0, column=1)
t1 = tkinter.Text(top, height=1, width=20)
t1.grid(row=0, column=2)


top.mainloop()
