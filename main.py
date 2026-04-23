import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Game(App):
    def build(self):
        self.secret = random.randint(1, 3)

        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Guess number 1 to 3")
        self.layout.add_widget(self.label)

        for i in range(1, 4):
            btn = Button(text=str(i))
            btn.bind(on_press=self.check)
            self.layout.add_widget(btn)

        return self.layout

    def check(self, instance):
        if int(instance.text) == self.secret:
            self.label.text = "🎉 Correct!"
        else:
            self.label.text = "❌ Wrong!"

Game().run()
