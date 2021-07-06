import tkinter as tk
from tkinter import ttk
import os
import datetime 
import sys
from termcolor import colored
import utils.customUtils as cu
from utils.customUtils import sysStatus, debugVar, debugMess, _convertPath
import poemFinder as pf

class PoetryGenerator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Initalise master window container (1x1 grid that expands in any direction) 
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Initialise secondary container (3x1 grid, all rows expand horizontally, top row can expand vertically also)
        main_container = tk.Frame(self, padx=30, pady=30, bg='pale green')
        main_container.grid(column=0, row=0, sticky = "nsew")
        main_container.grid_rowconfigure(0, weight = 1)
        main_container.grid_columnconfigure(0, weight = 1)

        # menu_bar = tk.Menu(main_container)
        # file_menu = tk.Menu(menu_bar, tearoff = 0) 
        # file_menu.add_command(label = "Save settings")
        # file_menu.add_separator()
        # file_menu.add_command(label = "Exit", command = quit)
        # menu_bar.add_cascade(label = "File", menu = file_menu)

        # tk.Tk.config(self, menu = menu_bar)

        # Get pageOne as an object by passing through its parameters
        # Then switch master window container to pageOne
        self.frames = {}
        for args in (PageOne,):
            frame = args(main_container, self)
            self.frames[args] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(PageOne)

    # Method to switch master window container to a new window object
    def show_frame(self, pointer):
        frame = self.frames[pointer]
        frame.tkraise()
    
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Initialise pageOne container (4x1 grid where all rows expand horizontally and row 1 expands vertically as well)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 1)
        self.rowconfigure(5, weight = 1)
        self.rowconfigure(6, weight = 1)
        self.columnconfigure(6, weight = 0)
        self.rowconfigure(7, weight = 1)
        self.rowconfigure(8, weight = 1)

        global startingPoem
        global numOfPoems
        global poemOrder

        # Initialising styling variables
        style = ttk.Style()
        style.configure('W.TLabel', font=('calibre', 20, 'normal'))
        style.configure('W.TEntry', font=('calibre', 20, 'normal'), relief=tk.FLAT, borderwidth=15)
        style.configure('W.TRadiobutton', font=('calibre', 20, 'normal'))
        style.configure('W.TButton', font=('calibre', 20, 'normal'))

        # Initialising variables
        numOfPoems = tk.StringVar()
        startingPoem = tk.StringVar()
        poemOrder = tk.StringVar()

        # Creating a title and assigning it to the first row of the window 
        titleLabel = ttk.Label(self, text = "Syllabary Poem Generator",  font=("Times New Roman", 40, 'italic'))
        titleLabel.grid(row = 0)

        # Creating user prompt for getting number of poems
        titleLabel = ttk.Label(self, text = "How many poems do you want to generate?", font=("calibre", 20, 'normal'))
        titleLabel.grid(row = 1)

        # User entry bar for getting number of poems
        poemNumEntry = ttk.Entry(self, textvariable=numOfPoems, font=('calibre', 20, 'normal'))
        poemNumEntry.grid(row = 2)

        # Creating user prompt for getting number of poems
        titleLabel = ttk.Label(self, text = "What poem do you wish to start with?", font=("calibre", 20, 'normal'))
        titleLabel.grid(row = 3)

        # User entry bar for getting poem order
        startingPoemEntry = ttk.Entry(self, textvariable=startingPoem, font=('calibre', 20, 'normal'))
        startingPoemEntry.grid(row = 4)

        # Creating user prompt for getting poem order
        titleLabel = ttk.Label(self, text = "Do you want to print out the poems starting or ending with this poems?", font=("calibre", 20, 'normal'))
        titleLabel.grid(row = 5)

        # Creating checkboxes to let the user input poem order
        radioButton1 = ttk.Radiobutton(self, text="starting", variable=poemOrder, value="forwards", style='W.TRadiobutton')
        radioButton2 = ttk.Radiobutton(self, text="ending", variable=poemOrder, value="backwards", style='W.TRadiobutton')
        radioButton1.grid(row = 6, column=0)
        radioButton2.grid(row = 6, column=1)    

        # Creating submit button
        submitButton = ttk.Button(self, text="Submit", command=lambda: self.submit()) 
        submitButton.grid(row = 7)

        # Creating exit button
        exitButton = ttk.Button(self, text="Exit", command=self.destroy) 
        exitButton.grid(row = 8)
    
    # Method that generates a list of files from the folder called 'syllabary_poems' based on the user inputs
    def runPoemFinder(self):
        inputDirectoryFilenameList = pf.createFileList(numOfPoems.get())
        max_values = pf.findMaxValues(inputDirectoryFilenameList)
        selectedPoemsList = pf.createOutputFileList(inputDirectoryFilenameList, startingPoem.get(), numOfPoems.get(), max_values)
        selectedPoemsList = pf.reverseList(poemOrder, selectedPoemsList)
        selectedPoemsDict = pf.readingXML(selectedPoemsList)
        pf.creatingTextDocumentOutput(selectedPoemsDict, selectedPoemsList)
        print("poem order is: " + str(poemOrder.get()))
    
    # When button is pressed call runPoemFinder
    def submit(self):
        self.runPoemFinder()


    
def main():
    syllabaryGenerator = PoetryGenerator()

    syllabaryGenerator.geometry("1280x720")
    syllabaryGenerator.title("Syllabary Poem Generator")
    #syllabaryGenerator.geometry("{}x{}".format(winfo_screenwidth(), winfo_screenheight())
    
    # Initialising global variables
    startingPoem = tk.StringVar()
    numOfPoems = tk.IntVar()
    poemOrder = tk.StringVar()

    syllabaryGenerator.mainloop()

    
if __name__ == "__main__":
    cu.preRunCleanUp()
    # sysStatus("Warning: this is a test warning")
    car1 = "string1 is me"
    # debugVar(car1)
    # debugMess("History is here")
    main()
    
    


