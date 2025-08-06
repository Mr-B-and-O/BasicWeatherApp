import requests # Our API for server requests
import tkinter # Our GUI. This module allows us to create windows and change the properties of text

'''
 So this program is going to be a basic weather program that will give the temperature and time for the city
they are in. So the program is going to have a simple window show up when it starts running so ill have to write
the graphics with tkinter functions. Next It is going to output text which will be edited by tkinter and
it will ask the user what city they are in so it can give the the time and the temperature. They input
it which then the program will send requests to the server and retrieve data through the requests API.
Then it will present the data which would be the time, and the temperature for that city. Ofcourse there
will also be exceptions to prevent crashes and it will have an executable. Will be on a loop so users can keep
requesting. I'll be uploading this on Git Hub as a repository and will be updating it till its done!
'''

print("Program is still in developing phases")
print("Greetings, please provide the city you're in "), input() # User inputs the city the reside in
print("Temperature is ") # Gives them the temperature
print("Time is ") # Gives them time

# The program will loop

