import tkinter as tk

root = tk.Tk()

# create a listbox
my_listbox = tk.Listbox(root)
for i in range(20):
    my_listbox.insert(tk.END, f"Item {i+1}")
my_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# create a scrollbar and connect it to the listbox
my_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=my_listbox.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
my_listbox.config(yscrollcommand=my_scrollbar.set)

root.mainloop()

# label = tkinter.Label(window, text="Hola mundo", bg = "green")
# # Coloca la eqtiqueta en la posicion indicada
# # side = tkinter.LEFT
# # label.pack(fill = tkinter.X)

# def hello(nombre):
#     print("Hello " + nombre)

# #button = tkinter.Button(window,text="Clic",padx=50,pady=50,command=hello)
# button1 = tkinter.Button(window,text="Hello",padx=50,pady=50,command=lambda: hello("Omar"))
# # button1.pack()

# # TextBox
# textbox = tkinter.Entry(window,font="Helvetica 12")
# # textbox.pack()

# def imprimir():
#     print(textbox.get())

# button2 = tkinter.Button(window,text='Get Text',command=imprimir)
# # button2.pack()

# button1.grid(row=0,column=0)
# textbox.grid(row=1,column=1)
# button2.grid(row=2,column=2)
# label.grid(row=1,column=0)
