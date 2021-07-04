import tkinter as tk
from tkinter import ttk
import os
import datetime 
import sys
from termcolor import colored
import poemFinder as pf

class PoetryGenerator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self is equal to root in this class (i.e. self.root)

        # Initalise master window container (1x1 grid that expands in any direction) 
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Set main container and make it take up the full area of the cell
        self.main_container = tk.Frame(self, padx=30, pady=30, bg='pale green')
        self.main_container.grid(column=0, row=0, sticky = "nsew")
        self.main_container.grid_rowconfigure(0, weight = 1)
        self.main_container.grid_columnconfigure(0, weight = 1)
        
        # Get pageOne as an object by passing through its parameters
        # Then switch master window container to pageOne
        self.frames = {}
        for args in (PageOne,):
            frame = args(self.main_container, self)
            self.frames[args] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(PageOne)

    # Method to switch master window container to a new window object
    def show_frame(self, pointer):
        frame = self.frames[pointer]
        frame.tkraise()

    # Method that generates a list of files from the folder called 'syllabary_poems' based on the user inputs
    def runPoemFinder(self):
        allPoemsList = pf.createFileList()
        max_values = pf.findMaxValues(allPoemsList)
        selectedPoemsList = pf.createOutputFileList(allPoemsList, self.startingPoem.get(), self.numOfPoems.get(), max_values)
        selectedPoemsList = pf.reverseList(self.poemOrder, selectedPoemsList)
        selectedPoemsDict = pf.readingXML(selectedPoemsList)
        pf.creatingTextDocumentOutput(selectedPoemsDict, selectedPoemsList)
        print("poem order is: " + str(self.poemOrder.get()))

    # When button is pressed call runPoemFinder
    def submit(self):
        self.runPoemFinder()
        self.root.destroy()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Initialise pageOne container (4x1 grid where all rows expand horizontally and row 1 expands vertically as well)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)

        # Creating a title and assigning it to the first row of the window 
        titleLabel = tk.Label(self, text = "Syllabary Poem Generator", font=("Times New Roman", 40, 'italic'))
        titleLabel.grid(row = 0, padx = 10, pady = 10)
                
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
    syllabaryGenerator = PoetryGenerator()

    syllabaryGenerator.geometry("1280x720")
    #syllabaryGenerator.geometry("{}x{}".format(winfo_screenwidth(), winfo_screenheight())

    syllabaryGenerator.mainloop()

    
if __name__ == "__main__":
    preRunCleanUp()
    main()
    
    


