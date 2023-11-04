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
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Geolocator")

        # Create a label for the public IP address entry
        self.public_ip_label = tk.Label(self.root, text="Public IP address:")
        self.public_ip_label.grid(row=0, column=0)

        # Create an entry widget for the public IP address
        self.public_ip_entry = tk.Entry(self.root)
        self.public_ip_entry.grid(row=0, column=1)

        # Create a button to geolocate the IP address
        self.geolocate_button = tk.Button(self.root, text="Geolocate", command=self.geolocate)
        self.geolocate_button.grid(row=1, column=0)

        # Create a text widget to display the IP whois information
        self.ip_whois_text = tk.Text(self.root)
        self.ip_whois_text.grid(row=2, column=0, columnspan=2)

        # Highlight the city, state, latitude, and longitude in green
        self.ip_whois_text.tag_config("region", foreground="green")
        self.ip_whois_text.tag_config("city", foreground="green")
        self.ip_whois_text.tag_config("latitude", foreground="green")
        self.ip_whois_text.tag_config("longitude", foreground="green")

    # Define a function to run the Geolocation on a target IP
    def geolocate(self):
        public_ip = self.public_ip_entry.get()

        # Get the IP whois information
        url = f"http://ipwhois.app/json/{public_ip}"
        response = requests.get(url)
        ip_whois = json.loads(response.content.decode("utf-8"))

        # Display the IP whois information
        self.ip_whois_text.delete("1.0", tk.END)
        for key, value in ip_whois.items():
            if key in ["region", "city", "latitude", "longitude"]:
                self.ip_whois_text.insert("end", f"{key}: {value}\n", (key,))
            else:
                self.ip_whois_text.insert("end", f"{key}: {value}\n")

        self.ip_whois_text.update()


def main():
    gui = GeolocatorGUI()
    gui.root.mainloop()


if __name__ == "__main__":
    main()
