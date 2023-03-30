import webbrowser
import time
from typing import Dict
from reportlab.pdfgen import canvas

URL = "https://linkedin.com/in/siddheshkulthe"

social_list = []

def Send_Message():
    # print("\nAmazing! Let's get your started :)")
    # name = str(input("Enter your name: "))
    # email = str(input("Enter your email: "))
    # phone = str(input("Enter your phone: "))
    # description = str(input("Enter your description: "))
    # choice2 = int(input("Do you want to add any social media links? (Y/N): "))
    # if choice2.lower() == "y":
    #     print("\nGot it!")
    #     linknumber = int(input("How many links do you want to enter? (Max 5): "))
    #     for i in range(linknumber):
    #         x = str(input("Enter your link number " + str(i+1) + ": "))
    user_info = {}
    user_info['name'] = input("Enter your name: ")
    user_info['email'] = input("Enter your email: ")
    user_info['phone'] = input("Enter your phone number: ")
    user_info['summary'] = input("Enter a summary of your skills and experience: ")
    user_info['education'] = input("Enter your education details: ")
    user_info['experience'] = input("Enter your work experience: ")
    user_info['skills'] = input("Enter your skills: ")
    # Generate the resume PDF
    output_path = user_info['name'].lower().replace(" ", "_") + "_resume.pdf"
    print("Your resume has been generated as:", output_path)

def Start():
    print("Do you want to make a")
    choice = int(input("1. Send Siddhesh A Message \n2. Check out Siddhesh\'s LinkedIn \nEnter (1/2): "))
    if choice == 1:
        Resume()
    elif choice !=1:
        print("\nCool! I'll lead you to his resume!")
        time.sleep(2)
        print("Btw, he's a super cool guy. Would really love to be friends with you :)")
        time.sleep(2)
        print("...")
        time.sleep(3)
        webbrowser.open(URL)


    # Define the resume template
    template = [
        ("Resume", "CENTER"),
        ("", "LINEBELOW"),
        ("", "PADDING", 20),
        ("Name: " + user_info['name'], ""),
        ("Email: " + user_info['email'], ""),
        ("Phone: " + user_info['phone'], ""),
        ("", "LINEBELOW"),
        ("Summary", "LEFT"),
        (user_info['summary'], "LEFT"),
        ("", "LINEBELOW"),
        ("Education", "LEFT"),
        (user_info['education'], "LEFT"),
        ("", "LINEBELOW"),
        ("Experience", "LEFT"),
        (user_info['experience'], "LEFT"),
        ("", "LINEBELOW"),
        ("Skills", "LEFT"),
        (user_info['skills'], "LEFT"),
    ]

    # Generate the resume PDF
    pdf_canvas = canvas.Canvas(output_path)
    pdf_canvas.setTitle("Resume - " + user_info['name'])
    pdf_canvas.setFont("Helvetica-Bold", 16)
    for line in template:
        if line[1] == "CENTER":
            pdf_canvas.drawCentredString(300, 750, line[0])
        elif line[1] == "LINEBELOW":
            pdf_canvas.line(30, pdf_canvas._y-20, 570, pdf_canvas._y-20)
        elif line[1] == "PADDING":
            pdf_canvas.setFont("Helvetica", 8)
            pdf_canvas.drawString(30, pdf_canvas._y-line[2], line[0])
            pdf_canvas.setFont("Helvetica-Bold", 10)
        else:
            pdf_canvas.setFont("Helvetica-Bold", 10)
            pdf_canvas.drawString(30, pdf_canvas._y-20, line[0])
            pdf_canvas.setFont("Helvetica", 10)
            pdf_canvas.drawString(180, pdf_canvas._y-20, line[1])
        pdf_canvas._y -= 30
    pdf_canvas.save()

Start()