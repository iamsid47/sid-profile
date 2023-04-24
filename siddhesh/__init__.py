import webbrowser
import time
import requests

URL = "https://linkedin.com/in/siddheshkulthe"
recipient_email = "siddheshkulthe43@gmail.com"

social_list = []

def send_message():
    message = str(input("Enter your message: "))
    print("...")
    time.sleep(1)
    print("Just so that Siddhesh can get back to you,")
    time.sleep(1)
    email = str(input("Please enter your email:"))
    vercel_url = "http://34.207.83.162:5000"
    data = {"message": message, "email" : email}

    # Make the HTTP POST request to your Vercel app's endpoint
    response = requests.post(vercel_url, json=data)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Error sending message.")


def start():
    print("Hey yo! Nice to meet you :)")
    time.sleep(1)
    print("What would you like to do?\n")
    time.sleep(1)
    choice = int(input("1. Send Siddhesh A Message \n2. Check out Siddhesh\'s LinkedIn \nEnter (1/2): "))
    if choice == 1:
        send_message()
    elif choice !=1:
        print("\nCool! I'll lead you to his resume!")
        time.sleep(2)
        print("Btw, he's a super cool guy. Would really love to be friends with you :)")
        time.sleep(2)
        print("...")
        time.sleep(3)
        webbrowser.open(URL)