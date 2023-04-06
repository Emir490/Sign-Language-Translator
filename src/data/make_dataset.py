import tkinter
import numpy as np
import os

SIGNS_PATH = os.path.join(r'src\data\categories')
capture_sign =''
categorie_selected=''
number_secuence = 0

window = tkinter.Tk()
window.geometry('400x400')
window.title('Capture Keypoints')

# Categories
Categories = ['ABC','Adjetivos, pronombres, preposiciones y articulos','Alimentos','Animales',
        'Calendario','Casa','Colores','Cuerpo humano','Escuela','Familia','Fruta y verduras',
        'Numeros','Palabras relacionadas','Republica Mexicana','Otras palabras']

Dic_Categories = {
    'ABC':'abc',
    'Adjetivos, pronombres, preposiciones y articulos':'adjetivos',
    'Alimentos':'alimentos',
    'Animales':'animales',
    'Calendario':'calendario',
    'Casa':'casa',
    'Colores':'colores',
    'Cuerpo humano':'cuerpo_humano',
    'Escuela':'escuela',
    'Familia':'familia',
    'Fruta y verduras':'frutas_verduras',
    'Numeros':'numeros',
    'Palabras relacionadas':'palabras_relacionadas',
    'Republica Mexicana':'republica_mexicana',
    'Otras palabras':'otras_palabras'
}


# Loads the array with the specified categorie
def load_Signs(categorie):
    array = np.load(os.path.join(SIGNS_PATH,categorie + '.npy'))
    return array

def select_sign(event):
    widget = event.widget
    if len(widget.curselection()) == 1:
        index = int(widget.curselection()[0])
        value = widget.get(index) # gets the value of the selected item in the listbox
        capture_sign = value
        print('You selected sign: ' + capture_sign)


# Displays the signs stated by the selected categorie
def display_Signs(event):
    widget = event.widget
    if len(widget.curselection()) == 1:
        index = int(widget.curselection()[0])
        value = widget.get(index)  # gets the value of the selected item in the listbox
        print('You selected categorie: ' + value)
        signs = load_Signs(Dic_Categories[value]) # loads all the signs
        listSigns.delete(0,tkinter.END)
        for sign in signs:
            listSigns.insert(tkinter.END,sign)    


def start_capture():
    print(categorie_selected)
    print(capture_sign)


# List Boxes
listCategories = tkinter.Listbox(window)
listCategories.bind('<<ListboxSelect>>',display_Signs)

listSigns = tkinter.Listbox(window)
listSigns.bind('<<ListboxSelect>>',select_sign)

for item in Categories:
    listCategories.insert(tkinter.END,item)

# UI elements
btnCapture = tkinter.Button(window,text='Iniciar Captura',command=start_capture)  # Button
lblSecuence = tkinter.Label(window,text='No. de Capturas')  # Label
txtSequence = tkinter.Entry(window,font='Arial 12')         # Textbox

# Create scrollbars
sbCategories = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=listCategories.yview)
listCategories.config(yscrollcommand=sbCategories.set)

sbSigns = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=listSigns.yview)
listSigns.config(yscrollcommand=sbSigns.set)

# Show Elements
btnCapture.place(anchor=tkinter.N,relx=0.5,y=5,height=25,width=100)
lblSecuence.place(anchor=tkinter.N,x=100,y=35,height=25,width=100)
txtSequence.place(anchor=tkinter.N,x=200,y=35,height=25,width=100)

listCategories.place(anchor=tkinter.N,x=95,y=65,height=300,width=180)
sbCategories.place(anchor=tkinter.N,x=185,y=65,height=300,width=15)

listSigns.place(anchor=tkinter.N,x=290,y=65,height=300,width=180)
sbSigns.place(anchor=tkinter.N,x=380,y=65,height=300,width=15)

# mainloop
window.resizable(False,False)
window.mainloop()