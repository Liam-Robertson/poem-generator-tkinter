import tkinter as tk
from tkinter import ttk
import os
import datetime 
import sys
from termcolor import colored
importFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'utils')
sys.path.append(importFilePath)
import utils.customUtils as cu
from utils.customUtils import sysStatus, debugVar, _convertPath
import poemFinder as pf

class PoetryGenerator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Initalise master window container (1x1 grid that expands in any direction) 
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Initialise secondary container (3x1 grid, all rows expand horizontally, top row can expand vertically also)
        main_container = tk.Frame(self, padx=30, pady=30, bg='floral white')
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

        # Initalise master window container (1x1 grid that expands in any direction) 
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Initialise secondary container (3x1 grid, all rows expand horizontally, top row can expand vertically also)
        mainSubframe = tk.Frame(self, bg='blanched almond', padx=100)
        mainSubframe.grid(column=0, row=0, sticky = "nsew")
        mainSubframe.grid_rowconfigure(0, weight = 1)
        mainSubframe.grid_columnconfigure(0, weight = 1)

        # Initialise pageOne container (4x1 grid where all rows expand horizontally and row 1 expands vertically as well)
        mainSubframe.columnconfigure(0, weight = 1)
        mainSubframe.rowconfigure(0, weight = 1)
        mainSubframe.rowconfigure(1, weight = 1)
        mainSubframe.rowconfigure(2, weight = 1)
        mainSubframe.rowconfigure(3, weight = 1)
        mainSubframe.rowconfigure(4, weight = 1)

        global startingPoem
        global numOfPoems
        global poemOrder

        mainSubframe.grid_rowconfigure(0, weight=1)
        mainSubframe.grid_columnconfigure(0, weight=1)

        # Create subcontainer 1 - number of poems
        subframe1 = tk.Frame(mainSubframe, bg='white',  relief=tk.RIDGE,  bd=5)
        subframe1.grid_columnconfigure(0, weight=1)
        subframe1.grid_rowconfigure(0, weight=1)
        subframe1.grid_rowconfigure(1, weight=1)
        subframe1.grid(row = 1, sticky = "nsew", pady=10)

        # Create subcontainer 2 - starting poem
        subframe2 = tk.Frame(mainSubframe, bg='white',  relief=tk.RIDGE,  bd=5)
        subframe2.grid_columnconfigure(0, weight=1)
        subframe2.grid_rowconfigure(0, weight=1)
        subframe2.grid_rowconfigure(1, weight=1)
        subframe2.grid(row = 2, sticky = "nsew", pady=10)

        # Create subcontainer 3 - radio buttons
        subframe3 = tk.Frame(mainSubframe, bg='white',  relief=tk.RIDGE,  bd=5)
        subframe3.grid_columnconfigure(0, weight=1)
        subframe3.grid_columnconfigure(1, weight=1)
        subframe3.grid_rowconfigure(0, weight=1)
        subframe3.grid_rowconfigure(1, weight=1)
        subframe3.grid(row = 3, sticky = "nsew", pady=10)

        # Create subcontainer 4 - submit and exit buttons
        subframe4 = tk.Frame(mainSubframe, bg='')
        subframe4.grid_columnconfigure(0, weight=1)
        subframe4.grid_rowconfigure(0, weight=1)
        subframe4.grid(row = 4, pady=20)

        # Create subcontainer for radio buttons
        radioSubframe = tk.Frame(subframe3, bg='white')
        radioSubframe.grid_columnconfigure(0, weight=1)
        radioSubframe.grid_columnconfigure(1, weight=1)
        radioSubframe.grid_rowconfigure(0, weight=1)
        radioSubframe.grid(row = 1)

        # Initialising styling variables
        style = ttk.Style()
        style.configure('W.TLabel', font=('calibre', 20, 'normal'), background='white')
        style.configure('W.TEntry', font=('calibre', 20, 'normal'), background='white', relief=tk.FLAT, borderwidth=15)
        style.configure('W.TRadiobutton', font=('calibre', 20, 'normal'), background='white')
        style.configure('W.TButton', font=('calibre', 20, 'normal'), height=100)

        # Initialising variables
        numOfPoems = tk.StringVar()
        startingPoem = tk.StringVar()
        poemOrder = tk.StringVar()

        # Creating a title and assigning it to the first row of the window 
        titleLabel = ttk.Label(mainSubframe, text = "Syllabary Poem Generator",  font=("Times New Roman", 40, 'italic'), background='floral white')
        titleLabel.grid(row = 0, pady=(0, 10), ipady=0, sticky = "nsew")
        titleLabel.configure(anchor='center')

        # Creating user prompt for getting number of poems
        titleLabel = ttk.Label(subframe1, text = "How many poems do you want to generate?", font=("calibre", 20, 'normal'), style='W.TLabel')
        titleLabel.grid(row = 0)

        # User entry bar for getting number of poems
        poemNumEntry = ttk.Entry(subframe1, textvariable=numOfPoems, font=('calibre', 20, 'normal'))
        poemNumEntry.grid(row = 1, pady=15)

        # Creating user prompt for getting number of poems
        titleLabel = ttk.Label(subframe2, text = "What poem do you want to select?", font=("calibre", 20, 'normal'), style='W.TLabel')
        titleLabel.grid(row = 0)

        # User entry bar for getting poem order
        startingPoemEntry = ttk.Entry(subframe2, textvariable=startingPoem, font=('calibre', 20, 'normal'))
        startingPoemEntry.grid(row = 1, pady=15)

        # Creating user prompt for getting poem order
        titleLabel = ttk.Label(subframe3, text = "Do you want the output poem list to start or end with the selected poem?", font=("calibre", 20, 'normal'), style='W.TLabel')
        titleLabel.grid(row = 0)

        # Creating checkboxes to let the user input poem order
        radioButton1 = ttk.Radiobutton(radioSubframe, text="Start", variable=poemOrder, value="forwards", style='W.TRadiobutton')
        radioButton2 = ttk.Radiobutton(radioSubframe, text="End", variable=poemOrder, value="backwards", style='W.TRadiobutton')
        radioButton1.grid(row = 1, column=0, padx=10, pady=10)
        radioButton2.grid(row = 1, column=1, padx=10, pady=10)    

        # Creating submit button
        submitButton = ttk.Button(subframe4, text="Submit", command=lambda: self.submit(), width=30, style='W.TButton') 
        submitButton.grid(row = 0)
    
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
    main()
    
    


