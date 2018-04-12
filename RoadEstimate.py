from tkinter import *
from tkinter import ttk
import urllib.request
from PIL import Image
import math



root = Tk()

content = ttk.Frame(root)
#frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=400, height=200)

titleLabel = ttk.Label(content, text="Road Surface Area Estimate")
latLabel = ttk.Label(content, text="Latitude")
longLabel = ttk.Label(content, text="Longitude")
desLabel = ttk.Label(content, text="Please enter the longitude and latitude of \n"
                                   "the center of the area you wish to estimate")


latVar = StringVar()  # Input variable for latitude
longVar = StringVar()  # Input variable for longitude
streetsVar = IntVar()
mainRoadsVar = IntVar()
freewaysVar = IntVar()
estVar = IntVar()


def calcArea(latVar, longVar, streetsVar, mainRoadsVar, freewaysVar):
	zoom = "17"
	url = "https://maps.googleapis.com/maps/api/staticmap?center=" + latVar + ",%" + longVar + "&zoom=17&size=6400x640&scale=2&style=feature:road|elements:labels.text|visibility:simplified|style=feature:all|element:labels|visibility:off&key=AIzaSyDrnO8uz948R97_bpojB81oCe-s7Bc6DNE"
	#url = "https://maps.googleapis.com/maps/api/staticmap?center=-37.787496,""%20145.124924&zoom=17&size=6400x640&scale=2&style=feature:road""|elements:labels.text|visibility:simplified|style=feature:all|" "element:labels|visibility:off&""key=AIzaSyDrnO8uz948R97_bpojB81oCe-s7Bc6DNE"
	pixelCount = 0

	urllib.request.urlretrieve(url, "map.png")
	im = Image.open("map.png")
	imageRGB = im.convert("RGB")
	aList = list(imageRGB.getdata())

	for i in range(len(aList)):
		if streetsVar == 1:
			if aList[i] == (254, 254, 254):  # White
				pixelCount += 1
		if mainRoadsVar == 1:
			if aList[i] == (255, 235, 175):  # Light yellow
				pixelCount += 1
		if freewaysVar == 1:
			if aList[i] == (254, 216, 157):  # Dark yellow
				pixelCount += 1


	mpp = 156543.03392 * math.cos(float(latVar) * math.pi / 180) / math.pow(2, int(zoom))  # Calculating metres per pixel

	global estVar
	estVar = int(pixelCount/mpp)
	estButton["text"] = estVar
	print(estVar)



lat = ttk.Entry(content, textvariable=latVar)
long = ttk.Entry(content, textvariable=longVar)
streets = ttk.Checkbutton(text="Streets", variable=streetsVar, onvalue=1, offvalue=0)
mainRoads = ttk.Checkbutton(text="Roads", variable=mainRoadsVar, onvalue=1, offvalue=0)
freeways = ttk.Checkbutton(text="Freeways", variable=freewaysVar, onvalue=1, offvalue=0)
estLabel = ttk.Label(content, textvariable=estVar)
estButton = ttk.Button(text="Estimate", command=lambda: calcArea(latVar.get(), longVar.get(), streetsVar.get(), mainRoadsVar.get(), freewaysVar.get()))

content.grid(column=0, row=0)
#frame.grid(column=0, row=0, columnspan=2, rowspan=9)
titleLabel.grid(column=0, row=0, columnspan=3)
desLabel.grid(column=1, row=1)
longLabel.grid(column=0, row=2)
latLabel.grid(column=0, row=3)
long.grid(column=1, row=2, columnspan=2)
lat.grid(column=1, row=3, columnspan=2)
streets.grid(column=0, row=4)
mainRoads.grid(column=0, row=5)
freeways.grid(column=0, row=7)
estButton.grid(column=0, row=8)
estLabel.grid(column=1, row=9)

root.mainloop()



