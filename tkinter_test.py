import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


# file explorer window
def browsefiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    if filename:
        file_info.configure(text=filename)
    else:
        pass


# First line
root = tk.Tk()

# configure root
root.title('VAT-Spy GeoJSON')
root.geometry('800x600')
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.iconbitmap('vattech.ico')

# tab control
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='DAT to GeoJSON')
tabControl.add(tab2, text='GeoJSON to DAT')

tabControl.pack(expand=1, fill="both")

# tab1
description = "Browse to a valid VAT-Spy firboundaries.dat file"
des_text = tk.Label(tab1, text=description)
des_text.grid(row=1, column=0, sticky=tk.W, pady=5, columnspan=2)

button_file = tk.Button(tab1, text='Browse', command=browsefiles)
button_file.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

file_info = tk.Label(tab1, text='No file selected')
file_info.grid(row=3, column=0, sticky=tk.W, pady=5, columnspan=2)

# categories = ['Work', 'Hobbies', 'Health', 'Bills']
# cat_label = tk.Label(tab1, text='Category: ')
# cat_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
# cat_inp = ttk.Combobox(tab1, values=categories)
# cat_inp.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
# cat_inp.current(2)
#
# cat_inp.bind("<<ComboboxSelected>>", lambda x: print('itemselected: {}'.format(cat_inp.get())))

# Last line
root.mainloop()
