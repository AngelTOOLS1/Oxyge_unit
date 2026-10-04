from kivy.app import App
from kivy.uix.label import Label

class MyLauncher(App):
    def build(self):
        return Label(text="Hello Launcher")

MyLauncher().run()
