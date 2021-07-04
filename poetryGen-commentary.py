import tkinter as tk
from tkinter import ttk
import os
import datetime 
import sys
from termcolor import colored
import poemFinder as pf

class PoetryGenerator(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Don't know what this does, will figure it out later. Probably auto initialises a root or something
        tk.Tk.__init__(self, *args, **kwargs)
        #self is equal to root in this class (i.e. self.root)

        # Set up a single container that can expand into space horizontally and vertically
        # I'm not sure why you do this, wouldn't this be default behaviour for a root? Apparently not if you're setting it here. This is probably pretty standard
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Set main container and make it take up the full area of the cell
        self.main_container = tk.Frame(self, padx=30, pady=30, bg='pale green')
        self.main_container.grid(column=0, row=0, sticky = "nsew")
        self.main_container.grid_rowconfigure(0, weight = 1)
        self.main_container.grid_columnconfigure(0, weight = 1)

        # This takes in PageOne as an object and loops over it's variables
        # It then creates a frame for each variable and sets it equal to the container
        # e.g. self.frames['title'] = tk.Label(self, text = "Syllabary Poem Generator", font=("Times New Roman", 40, 'italic'))
        # After this is completed switch the current window to PageOne
        self.frames = {}
        for args in (PageOne,):
            frame = args(self.main_container, self)
            self.frames[args] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(PageOne)

    # This takes in the parent page and the child window 
    # In TKinter you often have multiple windows 
    # tkraise the method used to switch current windows 
    def show_frame(self, pointer):
        frame = self.frames[pointer]
        frame.tkraise()


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

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # I think you set your different windows as separate classes. That seems reasonable. Guess I'll find out 

        # Create a root container that has three rows, all with the ability to expand into surrounding space horizontally. Row 1 also expands upwards
        # I guess you just do this because you know you have four things to initialise - title, graphs, page2 and exit
        # The title expanding upwards is also probably pretty standard, I imagine you always use that
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)

        # Creating a title and assigning it to the first row of the window (i.e. assigning it to self)
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
    
    


