import requests
from tkinter import *

# Okno
window = Tk()
window.minsize = (700, 400)
window.resizable(False, False)
window.title("ISS")

# Funkce
def iss_coordinates():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json() # json = způsob zápisu dat, přenosu dat, nezávislý na počítačové platformě. Rychlá komunikace, malý objem dat
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    longitude_label.config(text=f"Zeměpisná délka ISS je: {longitude}")
    latitude_label.config(text=f"Zeměpisná šířka ISS je: {latitude}")


# Vytvoření canvasu (canvas = maliřské plátno)
canvas = Canvas(window, width=500, height=280)
canvas.pack()
iss_img = PhotoImage(file="img/iss.gif")
canvas.create_image(0, 0, anchor="nw", image=iss_img)

# Framy
coordinates_frame = Frame(window)
coordinates_frame.pack()

# Tlačítko
recount_button = Button(coordinates_frame, text="Současné souřadnice ISS", command=iss_coordinates)
recount_button.pack()

# Labels
latitude_label = Label()
latitude_label.pack()

longitude_label = Label()
longitude_label.pack()



# hlavní cyklus
window.mainloop()





""" 



# print(data)
# print(data["message"]) # success
# print(data["timestamp"]) # 1695320175
# print(data["iss_position"]) # {'latitude': '-39.8646', 'longitude': '-105.9442'}


print(f"Současná zeměpisná šířka ISS je:{latitude}")
print(f"Současná zeměpisná délka ISS je:{longitude}") """