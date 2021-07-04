import tkinter as tk
from tkinter import ttk
import os
import datetime 
import sys
from termcolor import colored
import poemFinder as pf

class PoetryGenerator:
    def __init__(self, root):
        self.root = root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.frame = tk.Frame(self.root)
        self.subframe1 = tk.Frame(self.frame, borderwidth=5, relief=tk.RIDGE, bg='green')
        self.subframe2 = ttk.Frame(self.frame, borderwidth=30, relief=tk.RIDGE)
        self.subframe3 = ttk.Frame(self.frame, borderwidth=30, relief=tk.RIDGE)
        self.subframe4 = ttk.Frame(self.frame, borderwidth=30)
        

        style = ttk.Style()
        style.configure('W.TLabel', font=('calibre', 20, 'normal'))
        style.configure('W.TEntry', font=('calibre', 20, 'normal'), relief=tk.FLAT, borderwidth=15)
        style.configure('W.TRadiobutton', font=('calibre', 20, 'normal'))
        style.configure('W.TButton', font=('calibre', 20, 'normal'))
        
        self.root.title("Syllabary Poetry Generator")
        self.root.attributes("-fullscreen", True)

        self.startingPoem = tk.StringVar()
        self.numOfPoems = tk.IntVar()
        self.poemOrder = tk.StringVar()
        self.poemOrder.set(' ') 
        self.poemNumLabel = ttk.Label(self.subframe1, text="How many poems do you want to generate?", style='W.TLabel')
        self.poemNumEntry = ttk.Entry(self.subframe1, textvariable=self.numOfPoems, style='W.TEntry', font=('calibre', 15, 'normal'))
        self.startingPoemLabel = ttk.Label(self.subframe2, text="What poem do you want to start with?", style='W.TLabel')
        self.startingPoemEntry = ttk.Entry(self.subframe2, textvariable=self.startingPoem, style='W.TEntry', font=('calibre', 15, 'normal'))
        self.poemOrderLabel = ttk.Label(self.subframe3, text="Would you like to output the poems forwards or in reverse order?", style='W.TLabel')
        self.radioButton1 = ttk.Radiobutton(self.subframe3, text="forwards", variable=self.poemOrder, value="forwards", style='W.TRadiobutton')
        self.radioButton2 = ttk.Radiobutton(self.subframe3, text="backwards", variable=self.poemOrder, value="backwards", style='W.TRadiobutton')
        self.button = ttk.Button(self.subframe4, text="Submit", command=self.submit, style='W.TButton')
        self.exit_button = ttk.Button(self.subframe4, text="Exit Window", command=self.root.destroy, style='W.TButton')

            
    def setGrid(self):
        # Packing all objects so they can be viewed
        self.poemNumLabel.grid(row=0, column=0, pady=(0, 10), sticky='nesw')
        self.poemNumEntry.grid(row=1, column=0, pady=(5, 40), ipadx=220, ipady=5, sticky='nesw')
        self.startingPoemLabel.grid(row=2, column=0, pady=(0, 10), ipadx=10, sticky='nesw')
        self.startingPoemEntry.grid(row=3, column=0, pady=(5, 40), ipadx=20, ipady=5, sticky='nesw')
        self.poemOrderLabel.grid(row=4, column=0, pady=(0, 10), sticky='nesw')
        self.radioButton1.grid(row=5, column=0, pady=(5, 40), sticky='nesw')
        self.radioButton2.grid(row=5, column=1, pady=(5, 40), sticky='nesw')
        self.button.grid(row=6, column=0, pady=(10, 10), ipady=15, sticky='nesw')
        self.exit_button.grid(row=7, column=0, pady=(50, 0), ipady=15, columnspan=2, sticky='nesw')

        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.grid_rowconfigure(0, weight = 1)
        self.frame.grid_columnconfigure(0, weight = 1)

        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        #self.frame.grid_rowconfigure(0, weight=1)
        # self.subframe1.pack(fill="both", expand=True, padx=20, pady=20)
        #self.subframe1.grid()
        # self.subframe1.place(relx=0.5, rely=0.5, anchor='center')
        # self.subframe2.place(relx=0.5, rely=0.5, anchor='center')
        # self.subframe3.place(relx=0.5, rely=0.5, anchor='center')
        # self.subframe4.place(relx=0.5, rely=0.5, anchor='center')

        # self.subframe1.grid(row=1, column=0, sticky="nsew")
        self.subframe2.grid(row=1, column=0, sticky="nsew")
        self.subframe3.grid(row=2, column=0, sticky="nsew")
        self.subframe4.grid(row=3, column=0, sticky="nsew")

        # self.frame.grid_rowconfigure(0, weight=1)
        # self.frame.grid_rowconfigure(1, weight=1)
        # self.frame.grid_rowconfigure(2, weight=1)
        # self.frame.grid_rowconfigure(3, weight=1)

        
        # self.subframe1.grid(sticky='we')
        # self.root.grid_rowconfigure(0, weight=1)

        # self.subframe2.place(relx=0.5, rely=0.5, anchor='center')
        # self.subframe2.grid(sticky='we')
        # self.root.grid_rowconfigure(1, weight=1)

        # self.subframe3.grid(sticky='we')
        # self.root.grid_rowconfigure(2, weight=1)

        # self.subframe4.grid(sticky='we')
        # self.root.grid_rowconfigure(3, weight=1)

        # self.root.grid_rowconfigure(1, weight=1)
        
        
    
    def runPoemFinder(self):
        allPoemsList = pf.createFileList()
        max_values = pf.findMaxValues(allPoemsList)
        selectedPoemsList = pf.createOutputFileList(allPoemsList, self.startingPoem.get(), self.numOfPoems.get(), max_values)
        selectedPoemsList = pf.reverseList(self.poemOrder, selectedPoemsList)
        selectedPoemsDict = pf.readingXML(selectedPoemsList)
        pf.creatingTextDocumentOutput(selectedPoemsDict, selectedPoemsList)
        print("poem order is: " + str(self.poemOrder.get()))

    def submit(self):
        self.runPoemFinder()
        self.root.destroy()

    def styleFrame(self):
        return
        
def sysStatus(message, useTS=True, color='white'):
    #Cheap way of displaying timed status messages to terminal
    rawtime = datetime.datetime.now()
    timeStamp = rawtime.strftime('%Y-%m-%d %H:%M:%S')

    if useTS:
        #print(timeDisplay + colored(f'  {message}', 'green'))
        print(f'{timeStamp}:     {message}')
    else:
        print(colored(f'{message}', color))

def preRunCleanUp():
    #Clears out the terminal so you can easily view when the latest run was initiated
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('win'):
        os.system('cls')

    sysStatus('Run Started...\n')
    
def main():
    root = tk.Tk()

    syllabaryGenerator = PoetryGenerator(root)
    # syllabaryGenerator.grid(sticky="nsew")
    # root.grid_rowconfigure(0, weight=1)
    # root.grid_columnconfigure(0, weight=1)
    syllabaryGenerator.styleFrame()
    syllabaryGenerator.setGrid()
    

    root.mainloop()

    
if __name__ == "__main__":
    preRunCleanUp()
    main()
    
    


