import requests  # Our API for server requests
from tkinter import * # Our GUI. This module allows us to create windows and change the properties of text
from tkinter import ttk

'''
 So this program is going to be a basic weather program that will give the temperature and time for the city
they are in. So the program is going to have a simple window show up when it starts running so ill have to write
the graphics with tkinter functions. Next It is going to output text which will be edited by tkinter and
it will ask the user what city they are in so it can give the the time and the temperature (Maybe the temperature
and time wont appear on the window untill the user inputs the city, if so, it will be done in an if/else or do
statement). (I wonder how these inputs will interact with the API requests).They input it which then the program
will send requests to the server and retrieve data through the requests API.Then it will present the data which
would be the time, and the temperature for that city. Of course there will also be exeptions to prevent crashes
and it will have an executable. Will be on a loop so users can keep requesting. I'll be uploading this on Git Hub
as a repository and will be updating it till its done! - EMPR
'''

'''
 Dev Note 1: Alright, to have it so that when a user is prompted to write something in the program, like the what
city they are in, I want the text to be in a small frame and not plainly on the screen. It will make
it alot more "professional" and it's pretty much standard. So I'll have to change the grids into packs! - EMPR
'''

'''
 Dev Note 2: Welp I've added input and a simple HTTP requets as a test. From here it's now about actually getting data
the user types in using the requests funtions. After that, it will be getting the time and weather then after that, it's
creating loops so those text appear after certain actions have been done. I'll still have to figure out how to have everything
look neat but I'll worry about that after I get all the necessary code to the the tasks. This has been interesting so far in all
honesty and I'm proud of how I'm growing as a programmer! - EMPR
'''

'''
 Dev Note 3: I think ill be using the post method of requests to post data a site I want. Have whatever the user typed then
have that in the post method but if I find something better, that would be great. And to get data from a site, I can have
the URL then use the get method. Do i need to convert my data to Json? Is that a requirement so things work? To have the server respond
and load the page then after I just use get method to get specific data from the site? Do I need timeouts if my requess gets stuck?
Thats if it ever gets stuck. - EMPR
'''

'''
 Dev Note 4: So I can't use requests on certain sites which is not certified with requests like weathersa so i'm planning to
use a free weather API instead of requests. Should give me everyhting like location and time. Update: Okay you know what I think
I may have accidently stumbled upon a solution, so turns out i was going in the right directions with requests and what not!
I just needed to use it on a site that allows for it which is https://api.open-meteo.com/v1/forecast. So from what i learned
it's time to implement the HTTP things. - EMPR
'''

# Get the url of open-meteo then send data to it. The input of the user 

# First lets create the GUI elements
# Creating the window
root = Tk()  # Creates a top level window/root window which serves as the main window of the application
frm = ttk.Frame(root, padding =10)   # Creats a frame widget which the label and buttion will use
frm.pack()   # So we can have our elements be displayed in our window
root.geometry ("1290x720")    # Dimensions of the window
root.title("Check My Weather")    # Title of the program

# Creating functions and variables that will be needed for user inputs
def process_input():    # This will be called inside our button method
    user_input = entry_var.get()
    result_label.config(text=f"You entered: {user_input}")    # Telling user what they typed

# Our small window which text is going to be typed in
entry_var = StringVar() # Managing value of label widget to have our text
entry_widget = ttk.Entry(root, textvariable=entry_var, width=40)
entry_widget.pack(pady=10)



# Creating an object which will be used to add colours, and fonts to the text
style = ttk.Style()    # Style object for texts
style.configure(".", font=('Times New Roman', 30))    # Applies font and font size to all text. The lists of fonts: Arial, Times New Roman, Courier New, Verdana, Georgia, Tahoma, Comic Sans MS Impact
style.configure("Blue.TLabel", foreground ="blue")     # To add blue for labels
style.configure("Red.TLabel", foreground ="red")    # To add red for labels
style.configure("Purple.TLabel", foreground ="purple")    # To add purple for labels

# Using the request API to make a request (incomplete)
data = {"What" : "Huh"}
request = requests.post("https://www.weathersa.co.za/post", json=data)    # Send an HTTP GET request to a specified URL to retrieve data
text_from_site = request.text
result_label = Label(root, text="")    # The lebal for our process_input fucntion
result_label.pack(pady=10)

# Creating the text and button
greetings = ttk.Label(frm, text = "Greeting, please provide the city you're in ", style ="Blue.TLabel")    # Creates a label widget holding a static text string greeting the user
greetings.pack()
temperature = ttk.Label(frm, text = "Temperature is ", style ="Red.TLabel")    # Displaying the temperature
temperature.pack()
time = ttk.Label(frm, text = "Time is ", style ="Purple.TLabel")    # Displaying the time    
time.pack()
write_site_text = ttk.Label(root, text =f"{text_from_site}")    # Displaying the time    
write_site_text.pack()
botton_1 = ttk.Button(frm, text = "Input text test", command=process_input)    # A button widget is created . When pressed, it types out the text which the user typed
botton_1.pack(pady=10)
botton_2 = ttk.Button(frm, text = "Exit", command=root.destroy)    # A button widget is then created. When pressed, it will call the destroy() method on the root
botton_2.pack()


# Keeps the program running
root.mainloop()   # Method puts everything on the display, and responds to user input until the program terminates.

# The program will loop

# Ignore this part of the code. I may plan to use it so I'm keeping it here for now.

'''
# Is this the code I need to make my app work!? Did I stumble upon it by accident?! Remove longitude and latitude
# This code has potential but i need to figure out whats wrong, for whatever reason when I put in other time zones, it's not working except America/New_York

# Define the latitude and longitude for your desired location (e.g., New York City)
latitude = 25.7617
longitude = 1.1918

# Define the API endpoint and parameters
base_url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m",  # Request hourly temperature at 2 meters
    "forecast_days": 1,         # Get forecast for 1 day
    "timezone": "America/New_York" # Specify the timezone
}

try:
    # Make the API request
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    # Parse the JSON response
    data = response.json()

    # Extract and print the hourly temperatures
    if "hourly" in data and "time" in data["hourly"] and "temperature_2m" in data["hourly"]:
        times = data["hourly"]["time"]
        temperatures = data["hourly"]["temperature_2m"]

        print(f"Hourly temperatures for Latitude: {latitude}, Longitude: {longitude}")
        for i in range(len(times)):
            print(f"Time: {times[i]}, Temperature: {temperatures[i]}°C")
    else:
        print("Error: Could not retrieve hourly temperature data.")

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing JSON response: {e}")

'''
