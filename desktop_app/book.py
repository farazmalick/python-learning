import tkinter
import backend


def view_command():
    list1.delete(0, tkinter.END)
    for row in backend.view():
        list1.insert(tkinter.END, row)


def search_command():
    list1.delete(0, tkinter. END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(tkinter.END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get())
    view_command()


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, tkinter.END)
    e1.insert(tkinter.END, selected_tuple[1])
    e2.delete(0, tkinter.END)
    e2.insert(tkinter.END, selected_tuple[2])
    e3.delete(0, tkinter.END)
    e3.insert(tkinter.END, selected_tuple[3])
    e4.delete(0, tkinter.END)
    e4.insert(tkinter.END, selected_tuple[4])


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


def update_command():
    backend.update(selected_tuple[0], title_text.get(
    ), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


#####################################
top = tkinter.Tk()
top.wm_title("Book Store")
l1 = tkinter.Label(top, text="Tittle")
l1.grid(row=0, column=0)

l2 = tkinter.Label(top, text="Author")
l2.grid(row=0, column=2)

l3 = tkinter.Label(top, text="Year")
l3.grid(row=1, column=0)

l4 = tkinter.Label(top, text="ISBN")
l4.grid(row=1, column=2)

title_text = tkinter.StringVar()
e1 = tkinter.Entry(top, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = tkinter.StringVar()
e2 = tkinter.Entry(top, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = tkinter.StringVar()
e3 = tkinter.Entry(top, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = tkinter.StringVar()
e4 = tkinter.Entry(top, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = tkinter.Listbox(top, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = tkinter.Scrollbar(top)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = tkinter.Button(top, text="view all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = tkinter.Button(top, text="search", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = tkinter.Button(top, text="Add", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = tkinter.Button(top, text="update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = tkinter.Button(top, text="delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = tkinter.Button(top, text="close", width=12, command=top.destroy)
b6.grid(row=7, column=3)

top.mainloop()
