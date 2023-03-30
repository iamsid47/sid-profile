import webbrowser
import time
import smtplib

URL = "https://linkedin.com/in/siddheshkulthe"
recipient_email = "siddheshkulthe43@gmail.com"

social_list = []

def Send_Message():
    pass


def Start():
    print("Do you want to make a")
    choice = int(input("1. Send Siddhesh A Message \n2. Check out Siddhesh\'s LinkedIn \nEnter (1/2): "))
    if choice == 1:
        Send_Message()
    elif choice !=1:
        print("\nCool! I'll lead you to his resume!")
        time.sleep(2)
        print("Btw, he's a super cool guy. Would really love to be friends with you :)")
        time.sleep(2)
        print("...")
        time.sleep(3)
        webbrowser.open(URL)

Start()