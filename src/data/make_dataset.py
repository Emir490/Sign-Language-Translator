import tkinter

window = tkinter.Tk()
window.geometry("400x400")
# window.state("zoomed")

# List Boxes
listCategories = tkinter.Listbox(window)
listSigns = tkinter.Listbox(window)

# Elements of the listbox
list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL','M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(len(list)):
    listCategories.insert(tkinter.END,list[i])
    listSigns.insert(tkinter.END,list[i])

# Create scrollbars
sbCategories = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=listCategories.yview)
listCategories.config(yscrollcommand=sbCategories.set)

sbSigns = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=listSigns.yview)
listSigns.config(yscrollcommand=sbSigns.set)

# Show ListBoxes
listCategories.grid(row=1,column=0)
sbCategories.grid(row=1,column=1,sticky=tkinter.NS)

listSigns.grid(row=1,column=2)
sbSigns.grid(row=1,column=3,sticky=tkinter.NS)

# Show window
window.mainloop()