from app import Resume, Siddhesh
import webbrowser

URL = "https://linkedin.com/in/siddheshkulthe"

print("Do you want to make a")
choice = int(input("1. New Resume \n2. Check out Siddhesh\'s Resume?"))
if choice == 1:
    webbrowser.open(URL)
if choice !=1:
    Resume()