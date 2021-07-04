Debugging: 

Change background colour of frame: 
    main_container = tk.Frame(self, padx=30, pady=30, bg='green')


########################################################

Methods:

grid_rowconfigure:
allows you to set a weight for a given column {grid_rowconfigure(column, weight)}

########################################################

Properties:

.grid_rowconfigure(weight):
specifies what happens if there's extra space. If weight=1 then the row will grow to fill that extra space. If weight=0 it will stay fixed

.grid(sticky):
Sticky is also used when there's extra space. It indicates which side of the cell the widget will stick to. 
If sticky=N it will go to the top, if sticky=W it will go to the left
stick=NESW makes the grid take up all remaining space

Grid has a property called sticky. This defines 

########################################################

Combinations:

How to make a frame fill all possible space:
    self.grid_rowconfigure(0, weight=1) # this needed to be added
    self.grid_columnconfigure(0, weight=1) # as did this


***
Notes
***
When it comes to positioning your widgets - this could most easily be done by using grid. Essentially you would just 
think of a layout beforehand, split it all into square, use a grid to define those squares and that's it. You would create
empty space by defining objects as empty objects. 

You could do this but it seems fairly clumsy which is why I'm using containers which seems smoother but is much harder. 