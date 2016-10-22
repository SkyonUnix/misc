import math

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *

class pixel(Widget):
    pass

class particle(App):
    def build(self):
        return pixel()
        

if __name__ == '__main__':
    particle().run()