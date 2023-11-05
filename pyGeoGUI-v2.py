# Brandon Anderson
# ITT-111: Introduction to Information Technology - Topic-6
# Professor Ingrid Gaviria
#
# REFERENCES BELOW:
# Anderson, B. (2021, November 26). BASH Geolocator. GitHub.
#   https://github.com/phantompacket/python-geolocator/blob/main/pyGeoGUI.py
#
# Anderson, B. (2023, November 4). Python-Geolocator - pyGeoGUI.py. GitHub.
#   https://github.com/phantompacket/python-geolocator/blob/main/pyGeoGUI.py
#
# Bard. (2023). Python Geolocator GUI. [Large Language Model from Google AI].


import tkinter as tk
import requests
import json


# Create the GUI menu
class GeolocatorGUI:
    def __init__(geo_menu):
        geo_menu.root = tk.Tk()
        geo_menu.root.title("Geolocator")

        # Create a label for the public IP address entry
        geo_menu.public_ip_label = tk.Label(geo_menu.root, text="Public IP address:")
        geo_menu.public_ip_label.grid(row=0, column=0)

        # Create an entry widget for the public IP address
        geo_menu.public_ip_entry = tk.Entry(geo_menu.root)
        geo_menu.public_ip_entry.grid(row=0, column=1)

        # Create a button to geolocate the IP address
        geo_menu.geolocate_button = tk.Button(geo_menu.root, text="Geolocate", command=geo_menu.geolocate)
        geo_menu.geolocate_button.grid(row=1, column=0)

        # Create a text widget to display the IP whois information
        geo_menu.ip_whois_text = tk.Text(geo_menu.root)
        geo_menu.ip_whois_text.grid(row=2, column=0, columnspan=2)

        # Highlight the city, state, latitude, and longitude in green
        geo_menu.ip_whois_text.tag_config("region", foreground="green")
        geo_menu.ip_whois_text.tag_config("city", foreground="green")
        geo_menu.ip_whois_text.tag_config("latitude", foreground="green")
        geo_menu.ip_whois_text.tag_config("longitude", foreground="green")

    # Define a function to run the Geolocation on a target IP
    def geolocate(geo_menu):
        public_ip = geo_menu.public_ip_entry.get()

        # Get the IP whois information
        url = f"http://ipwhois.app/json/{public_ip}"
        response = requests.get(url)
        ip_whois = json.loads(response.content.decode("utf-8"))

        # Display the IP whois information
        geo_menu.ip_whois_text.delete("1.0", tk.END)
        for key, value in ip_whois.items():
            if key in ["region", "city", "latitude", "longitude"]:
                geo_menu.ip_whois_text.insert("end", f"{key}: {value}\n", (key,))
            else:
                geo_menu.ip_whois_text.insert("end", f"{key}: {value}\n")

        geo_menu.ip_whois_text.update()


def main():
    gui = GeolocatorGUI()
    gui.root.mainloop()


if __name__ == "__main__":
    main()
