# Brandon Anderson
# ITT-111: Introduction to Information Technology - Topic-6
# Professor Ingrid Gaviria
#
# REFERENCES BELOW:
# Anderson, B. (2023, November 4. BASH Geolocator. GitHub.
#   https://github.com/phantompacket/python-geolocator/blob/main/pyGeoGUI.py
#
# Anderson, B. (2023, November 4). Python-Geolocator - pyGeoGUI.py. GitHub.
#   https://github.com/phantompacket/python-geolocator/blob/main/pyGeoGUI.py
#
# Bard. (2023). Python Geolocator GUI. [Large Language Model from Google AI].

import pyfiglet
import requests
import json
import sys

# Define a function to retrieve the IPV4 address and store it into a variable
def get_public_ip():
    response = requests.get("http://ipecho.net/plain")  # If run without arguement, the script use my public IPv4
    public_ip = response.content.decode("utf-8")        # decode the output to UTF-8
    return public_ip    # return the output saved to {public_ip}

#Define a function to take the address saved to {public_ip} and issue GET request to ipwhois API
def get_ip_whois(public_ip):
    url = f"http://ipwhois.app/json/{public_ip}"    # save the address for the API to a variable called {URL}
    response = requests.get(url)    # GET request
    ip_whois = json.loads(response.content.decode("utf-8"))     # Convert the JSON data to UTF-8
    return ip_whois     # Return the output to the terminal

# Define the main function
def main():
    public_ip = get_public_ip() if len(sys.argv) == 1 else sys.argv[1] # If no arguement is supplied, run on my network

    # Print the title into ASCII art and credit my name
    print(pyfiglet.figlet_format("Geolocator", font="Slant"))   # Use pyfiglet module to turn script's title to ASCII art
    print("Author: Brandon Anderson")  # Basic print to credit my work

    ip_whois = get_ip_whois(public_ip)
    for key, value in ip_whois.items():
        print(f"{key}: {value}")    # Print the output from my request converted from JSON to UTF-8

if __name__ == "__main__":
    main()
