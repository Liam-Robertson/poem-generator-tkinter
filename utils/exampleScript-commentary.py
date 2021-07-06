import tkinter as tk
from tkinter import ttk
"""
LARGE_FONT = ("ariel", 20) # dont know what you had here

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        
        # Set root window to fill all empty space
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Set main container and make it take up the full area of the cell
        main_container = tk.Frame(self, padx=30, pady=30)
        main_container.grid(column=0, row=0, sticky = "nsew")
        main_container.grid_rowconfigure(0, weight = 1)
        main_container.grid_columnconfigure(0, weight = 1)

        # This dude was literally just creating a menu and adding a bunch of stuff to it. That's mildly disappoitning. 
        # I wonder what the advantages to a menu are. Should I be doing that? 
        # I doubt it, I think menus are only for button inputs 
        # I think you're going to have to figure this bit out for yourself, I don't think I can do this format 
        menu_bar = tk.Menu(main_container)
        file_menu = tk.Menu(menu_bar, tearoff = 0) 
        file_menu.add_command(label = "Save settings", command = lambda: popupmsg("Not supported yet!"))
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = quit)
        menu_bar.add_cascade(label = "File", menu = file_menu)

        tk.Tk.config(self, menu = menu_bar)

        self.frames = {}

        # MainPage is passed in here as an argument. I guess that makes sense. You have a script that runs your pages individually.
        # This is where he calls main page, presumably the comma is to show unnamed args. I need to figure out how that stuff works
        # This is kind of what you thought args did though. You pass in an unnamed number of args and initialize them with a for loop
        # This is actually very cool because it sort of means that you can automatically pass from one function to another without initialising variables. Is that right? 
        # I mean all these variables are hard coded in which is why you can pass them through without instantiating. Otherwise you'd have to instantiate 
        # I guess this also explains why no variables are self objects. I guess you only need to assign something to self if you plan on changing it. If it's hard coded in there's 
        # no point in assigning it to object variables. 
        # I mean I guess you still could. If it was me I'd stil have it in the constructor but I wouldn't pass them in as args. I think that's what I'll do 
        for fr in (MainPage,):
            frame = fr(main_container, self)
            self.frames[fr] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(MainPage)

    # I don't know what this does, something about execution order. I don't care for now. 
    def show_frame(self, pointer):
        frame = self.frames[pointer]
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # uncommented these lines
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)

        # These take in the root as an argument so they are still linked to this window
        # Yeah actually, these are initialised as self variables when they're passed in as self. Weird 
        # It feels like what you're passing from MainPage to script is actually the self.root. You set that up then pass it 
        # I guess that makes sense. The self.root is essentially the window itself so you pass that through as an object 
        # Yeah that's what this is. First it's initialised as an empty 4x1 grid then objects are assigned to the rows in that grid. Interesting.
        # I guess this page is passed to the script. The script then acts as a parent container and this is the child page 
        # I wonder how I would call this lable once it has been assigned to the object. self.Label? Not sure. 
        label = tk.Label(self, text = "Syllabary Poem Generator", font=("Times New Roman", 40, 'italic'))
        label.grid(row = 0, padx = 10, pady = 10)

        button1 = ttk.Button(self, text = "Graphs", command = lambda: controller.show_frame(GraphsPage))
        button1.grid(row = 1, sticky = 'nswe')

        button2 = ttk.Button(self, text = "Page 2", command = lambda: controller.show_frame(Page2))
        button2.grid(row = 2, sticky = 'nswe')

        button3 = ttk.Button(self, text = "Exit", command = quit)
        button3.grid(row = 3, sticky = 'nswe')

app = Main()
app.geometry("1280x720")
app.mainloop()

"""