from turtle import Turtle, Screen
import ingredients
import turtle
import time

class Report(Turtle):
    def __init__(self):
        super().__init__()
        self.water = ingredients.resources['water']
        self.milk = ingredients.resources['milk']
        self.coffee = ingredients.resources['coffee']

    def make_report(self):
        self.hideturtle()
        self.goto(-100,65)
        self.color("beige")
        self.write(f"Water = {self.water} ml\nMilk = {self.milk} ml\nCoffee = {self.coffee} g\nMoney = ${ingredients.profit}",align="left",font=("Arial",20,"normal"))

    def check_resources(self,user_drink):
        s = Screen()
        drink_ingredients = ingredients.MENU[user_drink]['ingredients']
        for key in drink_ingredients:
            if ingredients.resources[key] < drink_ingredients[key]:
                img="sad_coffee.gif"
                s.addshape(img)
                turtle.shape(img)
                self.goto(-90,0)
                self.color("beige")
                self.write(f"Sorry there is not enough {key}",align="left",font=("Arial",20,"normal"))
                return False
            else:
               return True


    def make_coffee(self,func_input):
        images = "load.gif"
        s = Screen()
        s.addshape(images)
        turtle.shape(images)
        time.sleep(3.0)
        user_drink = ingredients.MENU[func_input]['ingredients']
        for key in user_drink:
            ingredients.resources[key] -= user_drink[key]
        ready = "ready.gif"
        si = Screen()
        si.addshape(ready)
        turtle.shape(ready)
        self.write(f"Your Coffee is ready!Here is your {func_input}. Enjoy!",align="left",font=("Arial",20,"normal"))