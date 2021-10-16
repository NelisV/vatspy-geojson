import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from import_functions import dat_import
from export_functions import dat_export
import json
import webbrowser

load_dat_file = None
load_gj_file = None
save_gj_file = None
save_dat_file = None
settings = None

# TODO cleanup ununsed functions


# file explorer window
def load_dat():
    global load_dat_file
    local_filename = filedialog.askopenfilename(initialdir=settings['dat_dir'],
                                                title='Select a File',
                                                filetypes=(('FIRBoundaries.dat', '*.dat*'),))
    print(load_dat_file)
    if local_filename:
        load_dat_file = local_filename
        file_info.configure(text=load_dat_file)
        config('W')
        switch_btn_state('A', 1)
    else:
        file_info.configure(text=load_dat_file)


def load_gj():
    global load_gj_file
    local_filename = filedialog.askopenfilename(initialdir=settings['gj_dir'],
                                                title='Select a File',
                                                filetypes=(('FIRBoundaries GeoJSON', '*.GeoJSON*'),))
    print(load_gj_file)
    if local_filename:
        load_gj_file = local_filename
        file_info2.configure(text=load_gj_file)
        config('W')
        switch_btn_state('C', 1)
    else:
        file_info2.configure(text=load_gj_file)


def save_gj():
    global save_gj_file
    local_dirname = filedialog.asksaveasfilename(
        defaultextension='.geojson', filetypes=(('FIRBoundaries GeoJSON', '*.GeoJSON*'),),
        initialdir=settings['dat_dir'],
        title='Save As')

    if local_dirname:
        save_gj_file = local_dirname
        file_info3.configure(text=save_gj_file)
        if load_dat_file:
            switch_btn_state('B', 1)
    else:
        file_info3.configure(text=save_gj_file)


def save_dat():
    global save_dat_file
    local_dirname = filedialog.asksaveasfilename(
        defaultextension='.dat', filetypes=(('FIRBoundaries.dat', '*.dat*'),),
        initialdir=settings['gj_dir'],
        title='Save As')

    if local_dirname:
        save_dat_file = local_dirname
        file_info7.configure(text=save_dat_file)
        if load_gj_file:
            switch_btn_state('D', 1)
    else:
        file_info7.configure(text=save_dat_file)


# action to parse .dat file function
def parse_dat():
    try:
        dat_import(load_dat_file, save_gj_file)
        description4 = 'file saved to: ' + save_gj_file
        des_text4 = tk.Label(tab1, text=description4)
        des_text4.grid(row=6, column=0, sticky=sticky, pady=5, columnspan=col_span)

    except:
        print('parse error')
        description4 = 'Parsing error, check if you used a valid FIRBoundaries file'
        des_text4 = tk.Label(tab1, text=description4)
        des_text4.grid(row=6, column=0, sticky=sticky, pady=5, columnspan=col_span)


# action to parse .dat file function
def parse_gj():
    try:
        dat_export(load_gj_file, save_dat_file)
        description8 = 'file saved to: ' + save_dat_file
        des_text8 = tk.Label(tab1, text=description8)
        des_text8.grid(row=6, column=0, sticky=sticky, pady=5, columnspan=col_span)

    except:
        print('parse error')
        description8 = 'Parsing error, check if you used a valid FIRBoundaries geojson file'
        des_text8 = tk.Label(tab1, text=description8)
        des_text8.grid(row=6, column=0, sticky=sticky, pady=5, columnspan=col_span)


# action to switch button lock state
def switch_btn_state(button, state):
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
    if button == 'C':
        if state == 0:
            button_file7['state'] = tk.DISABLED
        if state == 1:
            button_file7['state'] = tk.NORMAL
    if button == 'D':
        if state == 0:
            button_datimport2['state'] = tk.DISABLED
        if state == 1:
            button_datimport2['state'] = tk.NORMAL


# create config file if it does not exist
def create_config():
    data = {
        'dat_dir': '/',
        'gj_dir': '/'
    }
    try:
        outfile = open('config.json', 'r')
        print('file found')
        with open('config.json') as f:
            data2 = json.load(f)
            print(data2['dat_dir'])
    except IOError:
        print('File not accessible')
        with open('config.json', 'w') as outfile:
            json.dump(data, outfile)
    finally:
        outfile.close()


# configuration saver/loader
def config(mode='R'):
    global settings
    if mode == 'W':

        if load_dat_file:
            defaultdir = load_dat_file.rsplit('/', 1)[0] + '/'
            settings['dat_dir'] = defaultdir

            with open('config.json', 'w') as outfile:
                json.dump(settings, outfile)

        elif load_gj_file:
            defaultdir = load_gj_file.rsplit('/', 1)[0] + '/'
            settings['gj_dir'] = defaultdir

            with open('config.json', 'w') as outfile:
                json.dump(settings, outfile)

    elif mode == 'R':
        with open('config.json', 'r') as readfile:
            settings = json.load(readfile)


def callback(url):
    webbrowser.open_new(url)


# ui formatting
col_span = 2
sticky = tk.NW


if __name__ == "__main__":
    # Load config file
    create_config()
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
    tab4 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='GeoJSON to VAT-Spy')
    tabControl.add(tab4, text='About')

    tabControl.pack(expand=1, fill="both")

    # --tab3--
    tab1.columnconfigure(1, weight=1)

    # load geojson file
    description1 = 'Browse to a valid GeoJSON containing FIR boundary data'
    des_text1 = tk.Label(tab1, text=description1)
    des_text1.grid(row=1, column=0, sticky=sticky, pady=5, columnspan=col_span)

    button_file2 = tk.Button(tab1, text='Browse', width=10, command=load_gj)
    button_file2.grid(row=2, column=0, sticky=sticky, padx=5, pady=5)

    file_info2 = tk.Label(tab1, text='No file selected')
    file_info2.grid(row=2, column=1, sticky=sticky, pady=5)

    # select a .dat save location
    description7 = 'FIRBoundaries.dat save location'
    des_text7 = tk.Label(tab1, text=description7)
    des_text7.grid(row=3, column=0, sticky=sticky, pady=5, columnspan=col_span)

    button_file7 = tk.Button(tab1, text='Save As', width=10, command=save_dat, state=tk.DISABLED)
    button_file7.grid(row=4, column=0, sticky=sticky, padx=5, pady=5)

    file_info7 = tk.Label(tab1, text='No directory selected')
    file_info7.grid(row=4, column=1, sticky=sticky, pady=5)

    # parse button
    button_datimport2 = tk.Button(tab1, text='Parse', width=10, command=parse_gj, state=tk.DISABLED)
    button_datimport2.grid(row=5, column=0, sticky=sticky, padx=5, pady=5)

    # --tab4-- about
    description5 = 'VAT-Spy - GeoJSON converter by NelisV'
    des_text5 = tk.Label(tab4, text=description5)
    des_text5.grid(row=1, column=0, sticky=sticky, pady=5, columnspan=2)

    description6 = 'Development - Alpha 2'
    des_text6 = tk.Label(tab4, text=description6)
    des_text6.grid(row=2, column=0, sticky=sticky, pady=5, columnspan=2)

    link1 = tk.Label(tab4, text='Program GitHub', fg='blue', cursor='hand2')
    link1.grid(row=4, column=0, sticky=sticky, pady=5, columnspan=2)
    link1.bind('<Button-1>', lambda e: callback('https://github.com/NelisV/vatspy-geojson'))

    link2 = tk.Label(tab4, text='VAT-Spy Data Project', fg='blue', cursor='hand2')
    link2.grid(row=5, column=0, sticky=sticky, pady=5, columnspan=2)
    link2.bind('<Button-1>', lambda e: callback('https://github.com/vatsimnetwork/vatspy-data-project'))

    # mainloop
    root.mainloop()
