import tkinter as tk
from tkinter import ttk
import os
import datetime 
import sys
from termcolor import colored
import poemFinder as pf

class PoetryGenerator(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        #mainFrame = Frame(self, bg='blue')
        # Initialising all input objects, properties and labels
        #self.root = root
        #self.root.geometry("1000x1000")
        #pad=3
        #self.root.geometry("{0}x{1}".format(self.root.winfo_screenwidth()-pad, self.root.winfo_screenheight()-pad))
            # self.title("Syllabary Poetry Generator")
            # self.attributes("-fullscreen", True)
        # mainFrame = tk.Frame(self.root,bg="blue")

        self.startingPoem = tk.StringVar()
        self.numOfPoems = tk.IntVar()
        self.poemOrder = tk.StringVar()
        self.poemOrder.set(' ') 
        self.poemNumLabel = tk.Label(self, text="How many poems do you want to generate?", bg='green')
        self.poemNumEntry = tk.Entry(self, textvariable=self.numOfPoems, font=('calibre', 10, 'normal'))
        self.startingPoemLabel = tk.Label(self, text="What poem do you want to start with?", bg='green')
        self.startingPoemEntry = tk.Entry(self, textvariable=self.startingPoem, font=('calibre', 10, 'normal'))
        self.poemOrderLabel = tk.Label(self, text="Would you like to output the poems forwards or in reverse order?", bg='green')
        self.radioButton1 = tk.Radiobutton(self, text="forwards", variable=self.poemOrder, value="forwards")
        self.radioButton2 = tk.Radiobutton(self, text="backwards", variable=self.poemOrder, value="backwards")
        self.button = tk.Button(self, text="Submit", command=self.submit)
        self.exit_button = tk.Button(self, text="Exit Window", command=self.destroy)

        # tk.Frame.__init__(self, parent)
        # label = tk.Label(self, text="This should be centered")
        # label.grid(row=1, column=1)
        
        
        # self.grid(row=0, column=0, sticky="NESW")
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        # self.root.grid_rowconfigure(0, weight=1)
        # self.root.grid_columnconfigure(0, weight=1)
        

            
    def packFrame(self):
        # Packing all objects so they can be viewed
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.poemNumLabel.grid()
        self.poemNumEntry.grid()
        self.startingPoemLabel.grid()
        self.startingPoemEntry.grid()
        self.poemOrderLabel.grid()
        self.radioButton1.grid()
        self.radioButton2.grid()
        self.button.grid()
        self.exit_button.grid()
    
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
        style = ttk.Style()
        style.theme_use("clam")
        # self.root.grid_rowconfigure(0, weight=1)
        # self.root.grid_columnconfigure(0, weight=1)
        # self.root.grid_columnconfigure(0, weight=1)
        # self.root.grid_rowconfigure(0, weight=1)
        # self.root.config(height=500, width=500)
        # style = tk.Canvas(self.root, bg = 'red', height=100, width=100)
        # style.place(relx=0.5, rely=0.5, anchor=CENTER)
        
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
    syllabaryGenerator.grid(sticky="nsew")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    syllabaryGenerator.packFrame()
    syllabaryGenerator.styleFrame()

    root.mainloop()
    
if __name__ == "__main__":
    preRunCleanUp()
    main()
    

