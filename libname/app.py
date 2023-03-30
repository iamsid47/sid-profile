import webbrowser
import time
import requests

URL = "https://linkedin.com/in/siddheshkulthe"
recipient_email = "siddheshkulthe43@gmail.com"

social_list = []

def Send_Message():
    # Define the message to send
    message = "Hello, this is a message sent from Python!"

    # Define the URL of your Vercel app's endpoint
    vercel_url = "https://your-vercel-app.vercel.app/api/send-email"

    # Define the data to send in the POST request
    data = {"message": message}

    # Make the HTTP POST request to your Vercel app's endpoint
    response = requests.post(vercel_url, json=data)

    # Check the response status code
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Error sending message.")


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