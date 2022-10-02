from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import random


def get_number():
    red_balls = [i for i in range(1, 34)]
    blue_balls = [i for i in range(1, 17)]
    red = []
    for i in range(0, 6):
        red_index = random.randint(0, len(red_balls) - 1)
        red.append(red_balls.pop(red_index))
    red.sort()
    blue_index = random.randint(0, 15)
    blue = blue_balls[blue_index]
    double_ball_result = red + [blue]
    return '  '.join([str(i) for i in double_ball_result])


class DoubleBallApp(App):
    def build(self):
        root_widget = BoxLayout(orientation='vertical')
        number01 = '2  3  9  12  16  24  1'
        lable01 = Label(text=number01, font_size=70)
        number02 = get_number()
        lable02 = Label(text=number02, font_size=70)
        root_widget.add_widget(lable01)
        root_widget.add_widget(lable02)

        return root_widget


if __name__ == '__main__':
    DoubleBallApp().run()
