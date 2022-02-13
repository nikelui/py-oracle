import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.clock import Clock
from random import randint

class MainMenu(Widget):
    pass

class oracleApp(App):
    def build(self):
        self.load_kv('oracle.kv')
        start = MainMenu()
        return start

if __name__ == '__main__':
    oracleApp().run()