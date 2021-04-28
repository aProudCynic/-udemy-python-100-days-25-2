from turtle import Turtle

NAME_POSITION_INDEX = 0
X_POSITION_INDEX = 1
Y_POSITION_INDEX = 2

class StateDisplay(Turtle):

    def __init__(self, state):
        state_as_list = state.values.tolist()[0]
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(float(state_as_list[X_POSITION_INDEX]), float(state_as_list[Y_POSITION_INDEX]))
        self.text = state_as_list[NAME_POSITION_INDEX]
        self.write(self.text, align='center', font=('Arial', 10))
