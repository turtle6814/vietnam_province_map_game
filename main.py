import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Vietnam Map Game")

image = "Vietnam_location_map.gif"
screen.addshape(image)
screen.setup(width=600, height=783)
turtle.shape(image)

data = pd.read_csv("vietnam_provinces_coordinates.csv")
all_provinces = data.province.to_list()
guess_provinces = []

while len(guess_provinces) < 63:
    answer_province = screen.textinput(title=f"{len(guess_provinces)}/63 Provinces Correct",
                                    prompt="What's another province's name?").title()

    if answer_province == "Exit":
        missing_province = []
        for province in all_provinces:
            if province not in guess_provinces:
                missing_province.append(province)
        break
    if answer_province in all_provinces:
        guess_provinces.append(answer_province)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.province == answer_province]
        t.goto(int(province_data.x), int(province_data.y))
        t.write(province_data.province.item(), font=("Arial", 6, "normal"))



# def get_mouse_click_coor(x, y):
#     """Get the coordinates of the mouse from the map"""
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


# screen.exitonclick()