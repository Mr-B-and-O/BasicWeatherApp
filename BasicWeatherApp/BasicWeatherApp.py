import requests  # Our API for server requests
from tkinter import * # Our GUI. This module allows us to create windows and change the properties of text
from tkinter import ttk

'''
 So this program is going to be a basic weather program that will give the temperature and time for the city
they are in. So the program is going to have a simple window show up when it starts running so ill have to write
the graphics with tkinter functions. Next It is going to output text which will be edited by tkinter and
it will ask the user what city they are in so it can give the the time and the temperature. They input
it which then the program will send requests to the server and retrieve data through the requests API.
Then it will present the data which would be the time, and the temperature for that city. Of coarse their
will also be exeptions to prevent crashes and it will have an executable. Will be on a loop so users can keep
requesting. I'll be uploading this on Git Hub as a repository and will be updating it till its done!
'''

root = Tk()  # Creates a top level window/root window which serves as the main window of the application
frm = ttk.Frame(root, padding =10)   # Creats a frame widget which the label and buttion will use
frm.grid()   # So we can have our elements be displayed in our window
ttk.Label(frm, text = "Greeting, please provide the city you're in ").grid(column =6,row =0) # Creates a label widget holding a static text string greeting the user
ttk.Label(frm, text = "Temperature is ").grid(column =7,row =4)     # Displaying the temperature
ttk.Label(frm, text = "Time is ").grid(column =6,row =4)    # Displaying the time    
ttk.Button(frm, text = "Exit", command=root.destroy).grid(column =9, row =10)    # A button widget is then created. When pressed, it will call the destroy() method on the root
root.title("Check My Weather")    # Title of the program
root.geometry ("430x80")    # The window dimensions                                                           
root.mainloop()   # Method puts everything on the display, and responds to user input until the program terminates.

# The program will loop
