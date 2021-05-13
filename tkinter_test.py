import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from main import dat_import
import json
import webbrowser

filename = None
dirname = None
settings = None


# file explorer window
def browsefiles():
    global filename
    local_filename = filedialog.askopenfilename(initialdir=settings['dat_dir'],
                                          title="Select a File",
                                          filetypes=(("FIRBoundaries.dat", "*.dat*"), ("all files", "*.*")))
    print(filename)
    if local_filename:
        filename = local_filename
        file_info.configure(text=filename)
        config('W')
        switchButtonState('A', 1)
    else:
        file_info.configure(text=filename)


def browsedirectory():
    global dirname
    local_dirname = filedialog.asksaveasfilename(
                defaultextension='.geojson', filetypes=[("GeoJSON files", '*.geojson')],
                initialdir=settings['dat_dir'],
                title="Save As")

    if local_dirname:
        dirname = local_dirname
        file_info3.configure(text=dirname)
        if filename:
            switchButtonState('B', 1)
    else:
        file_info3.configure(text=dirname)


# action to call function
def datparser():
    try:
        dat_import(filename, dirname)
        description4 = "file saved to: " + dirname
        des_text4 = tk.Label(tab1, text=description4)
        des_text4.grid(row=6, column=0, sticky=tk.W, pady=5, columnspan=2)

    except:
        print('parse error')
        description4 = 'Parsing error, check if you used a valid FIRBoundaries file'
        des_text4 = tk.Label(tab1, text=description4)
        des_text4.grid(row=6, column=0, sticky=tk.W, pady=5, columnspan=2)


# action to display parse button
def switchButtonState(button, state):
    if button == 'A':
        if state == 0:
            button_file3['state'] = tk.DISABLED
        if state == 1:
            button_file3['state'] = tk.NORMAL
    if button == 'B':
        if state == 0:
            button_datimport['state'] = tk.DISABLED
        if state == 1:
            button_datimport['state'] = tk.NORMAL


# configuration saver/loader
def config(mode='R'):
    global settings
    if mode == 'W':

        if filename:
            defaultdir = filename.rsplit('/', 1)[0]+'/'
            settings['dat_dir'] = defaultdir

            with open('config.json', 'w') as outfile:
                json.dump(settings, outfile)
    elif mode == 'R':
        with open('config.json', 'r') as readfile:
            settings = json.load(readfile)


def callback(url):
    webbrowser.open_new(url)


# Load config file
config()

# First line
root = tk.Tk()

# configure root
root.title('VAT-Spy GeoJSON')
root.geometry('500x400')
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.iconbitmap('vattech.ico')

# tab control
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='DAT to GeoJSON')
tabControl.add(tab2, text='GeoJSON to DAT')
tabControl.add(tab3, text='About')

tabControl.pack(expand=1, fill="both")

# tab1
# load firboundaries.dat file
description = "Browse to a valid VAT-Spy firboundaries.dat file"
des_text = tk.Label(tab1, text=description)
des_text.grid(row=1, column=0, sticky=tk.W, pady=5, columnspan=2)

button_file = tk.Button(tab1, text='Browse', command=browsefiles)
button_file.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

file_info = tk.Label(tab1, text='No file selected')
file_info.grid(row=2, column=1, sticky=tk.W, pady=5, columnspan=2)

# select a save location
description3 = "GeoJSON save location"
des_text3 = tk.Label(tab1, text=description3)
des_text3.grid(row=3, column=0, sticky=tk.W, pady=5, columnspan=2)

button_file3 = tk.Button(tab1, text='Save As', command=browsedirectory, state=tk.DISABLED)
button_file3.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

file_info3 = tk.Label(tab1, text='No directory selected')
file_info3.grid(row=4, column=1, sticky=tk.W, pady=5, columnspan=2)

button_datimport = tk.Button(tab1, text='Parse', command=datparser, state=tk.DISABLED)
button_datimport.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)

# tab about
description5 = "VAT-Spy - GeoJSON converter by NelisV"
des_text5 = tk.Label(tab3, text=description5)
des_text5.grid(row=1, column=0, sticky=tk.W, pady=5, columnspan=2)

description6 = "Development - Alpha 1"
des_text6 = tk.Label(tab3, text=description6)
des_text6.grid(row=2, column=0, sticky=tk.W, pady=5, columnspan=2)

link1 = tk.Label(tab3, text="Program GitHub", fg="blue", cursor="hand2")
link1.grid(row=4, column=0, sticky=tk.W, pady=5, columnspan=2)
link1.bind("<Button-1>", lambda e: callback("https://github.com/NelisV/vatspy-geojson"))

link2 = tk.Label(tab3, text="VAT-Spy Data Project", fg="blue", cursor="hand2")
link2.grid(row=5, column=0, sticky=tk.W, pady=5, columnspan=2)
link2.bind("<Button-1>", lambda e: callback("https://github.com/vatsimnetwork/vatspy-data-project"))

root.mainloop()
