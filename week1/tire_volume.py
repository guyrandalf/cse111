import math
from datetime import datetime

width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * (width ** 2) * ratio * (width * ratio + 2540 * diameter)) / 10000000000

print(f"The approximate volume is {volume:.2f} liters")

customer_answer = ""
customer_name = ""
customer_phone = ""

while customer_answer != "yes" or customer_answer != "no":
    customer_answer = input("Do you want to buy a tire with inserted dimensions? (Yes(y)/No(n)): ")

    if customer_answer.lower() == "yes" or customer_answer.lower() == "y":
        customer_name = input("Great choice!\nPlease, insert your name: ")
        customer_phone = input("Please, insert your phone number: ")
        print("Thanks!")
        break;

    elif customer_answer.lower() == "no" or customer_answer.lower() == "n":
        print("Ok!")
        break;


current_date = datetime.now()
with open("volumes.txt", mode="at") as volume_file:

    print(f"Date: {current_date:%Y-%m-%d} \nWidth: {width} \nRatio: {ratio} \nDiameter: {diameter} \nVolume: {volume:.2f}",file=volume_file)

    if customer_name != "" or customer_phone != "":
        print(f"Customer name: {customer_name}\nCustomer phone number: {customer_phone}\n\n", file=volume_file)

    