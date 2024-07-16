import tkinter as tk
from PIL import ImageTk, Image
from geopy.geocoders import Nominatim

def get_lat_long():
    location = entry.get()
    geolocator = Nominatim(user_agent="geo_locator")
    try:
        location_info = geolocator.geocode(location)
        latitude = location_info.latitude
        longitude = location_info.longitude
        result_label.config(text=f"Latitude: {latitude}\nLongitude: {longitude}")
    except AttributeError:
        result_label.config(text="Location not found.")

# Create the main window
root = tk.Tk()
root.title("Location to Lat/Long")
root.geometry("600x400")
# Load background image
background_image = Image.open("/home/tomato/coder/learn/gui projects/project2/background_image.jpeg")
background_photo = ImageTk.PhotoImage(background_image)

# Set background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

text_label = tk.Label(root, text="Real Flagit", fg='black', bg='#03c2fc')
text_label.pack(pady=(10, 10))
text_label.config(font=("Vandana", 25))

# Create and place widgets
label = tk.Label(root, text="ENTER LOCATION", bg='#03c2fc')
label.pack(pady=(30,10))
label.config(font=("Arial",14))

entry = tk.Entry(root)
entry.pack()
entry.config(font=("Arial",14))

button = tk.Button(root, text="Get Lat/Long", command=get_lat_long, bg='#03c2fc')
button.pack(pady=(10,30))
button.config(font=("Arial",14))


result_label = tk.Label(root, text="", bg='#03c2fc')
result_label.pack()
result_label.config(font=("Arial",14))


# Start the main event loop
root.mainloop()
