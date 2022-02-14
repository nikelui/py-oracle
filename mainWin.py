import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

class MainMenu(Screen):
    pass

class MainOracle(Screen):
    pass

class LoadOracle(Screen):
    pass

class Settings(Screen):
    pass

class oracleApp(App):
    def build(self):
        Window.size = (300, 535)  # DEBUG (smartphone ratio: 16/9). Comment this line before building
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(MainOracle(name='oracle'))
        sm.add_widget(LoadOracle(name='load'))
        sm.add_widget(Settings(name='settings'))

        return sm

if __name__ == '__main__':
    oracleApp().run()