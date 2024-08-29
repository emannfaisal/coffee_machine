import ingredients
import turtle
import time
from report import Report
from payment import Payment
r=Report()
pay = Payment()
screen=turtle.Screen()
screen.setup(650,590)

image_rep = "Madelyn Rough (1).gif"

def change_image():
    screen.addshape(image_rep)
    turtle.shape(image_rep)




def main():
    images = "download.gif"
    screen.addshape(images)
    turtle.shape(images)
    time.sleep(0.3)

    user_input = screen.textinput("make choice","What would you like to have? (Espresso/Latte/Cappuccino?): ").lower()
    if user_input != "off":
        if user_input == "report":
            change_image()
            r.make_report()
        else:
            if r.check_resources(user_input):
                user_money = pay.process_payment()
                if pay.transaction_successful(user_input, user_money):
                    r.make_coffee(user_input)





main()
screen.exitonclick()

