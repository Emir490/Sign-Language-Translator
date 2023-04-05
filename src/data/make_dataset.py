import tkinter

window = tkinter.Tk()
window.geometry("400x400")
# window.state("zoomed")

list_box = tkinter.Listbox(window)

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL','M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(len(list)):
    list_box.insert(tkinter.END,list[i])

list_box.pack()
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

window.mainloop()