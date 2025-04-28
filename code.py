import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import os
from io import StringIO
from re import IGNORECASE
import sys
import random
import contextlib
import time



def exec_res(text):
    try:
        with stdout_io() as s:
            exec(text)
        return(s.getvalue())
    except Exception as e:
        return(str(e))
    

@contextlib.contextmanager
def stdout_io(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

class MyApp(App):
    def build(self):
        self.title = "PyExec"
        Window.clearcolor = (0.07,0.07,0.07,1)
        layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput( multiline=True,size_hint=(.9,0.66),pos_hint={'x':.05,'y':0.1},foreground_color=(0.9,.933,0.9,0.9),background_color=(0.1,.1,0.1,0.9))
        submit_button = Button(text='run',on_press=self.on_button_click,size_hint=(0.05,0.05),pos_hint={'x':0.90,'y':0},background_color=(0.324,.933,0.230,0.9))
        self.text_rez = TextInput(text='TERMINAL:\n', multiline=True,size_hint=(.9,0.3),pos_hint={'x':.05,'y':0.01},foreground_color=(0.9,.933,0.9,0.9),background_color=(0.07,.07,0.07,0.78))
        self.input_label3 = Label(text='Create by :@pycode_hub',size_hint=(1,0.05),outline_color=(1,0.1,.2,1))
        layout.add_widget(submit_button)
        layout.add_widget(self.text_input)
        layout.add_widget(self.text_rez)
        layout.add_widget(self.input_label3)
        return layout

    def on_button_click(self, instance):
        user_text = self.text_input.text
        self.text_rez.text = self.text_rez.text  + '\n'+exec_res(user_text)
        
    




if __name__ == '__main__':
    MyApp().run()
