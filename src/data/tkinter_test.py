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