import turtle
from turtle import Turtle,Screen
import ingredients
class Payment(Turtle):
    def __init__(self):
        super().__init__()
        s = Screen()
    def process_payment(user):
        image_pay = "payment.gif"
        s=Screen()
        s.addshape(image_pay)
        turtle.shape(image_pay)
        quarters = int(s.textinput("Enter money","quarters: "))
        dimes = int(s.textinput("Enter money","dimes: "))
        nickles = int(s.textinput("Enter money","nickles: "))
        pennies = int(s.textinput("Enter money","pennies: "))
        total_money = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)
        return total_money

    def transaction_successful(self,func_drink, user_payment):
        if user_payment < ingredients.MENU[func_drink]['cost']:
            sad_img = "sad_coffee.gif"
            s = Screen()
            s.addshape(sad_img)
            turtle.shape(sad_img)
            self.goto(-90,0)
            self.write("Sorry that is not enough money. Money refunded",align="left",font=("Arial",16,"normal"))
            return False
        else:
            ingredients.profit += ingredients.MENU[func_drink]['cost']
            if user_payment > ingredients.MENU[func_drink]['cost']:
                change = round(user_payment - ingredients.MENU[func_drink]['cost'], 2)
                self.color("Beige")
                self.goto(-90,0)
                self.write(f"Here is {change} dollars\n in change",align="left",font=("Arial",16,"normal"))
                return True

