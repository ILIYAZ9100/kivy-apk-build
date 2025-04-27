from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.result = Label(text="", font_size=32, halign="right", valign="center")
        self.result.bind(size=self.result.setter('text_size'))
        
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        layout.add_widget(self.solution)
        layout.add_widget(self.result)
        
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)
        
        return layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
            self.solution.text = ""
            self.result.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators
            ):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        try:
            if text:
                # Replace unicode characters with Python operators
                expression = text.replace("×", "*").replace("÷", "/")
                solution = str(eval(expression))
                self.result.text = solution
                self.solution.text = solution
        except Exception as e:
            self.show_error_popup(str(e))
            self.solution.text = ""
            self.result.text = ""

    def show_error_popup(self, error_message):
        content = Label(text=f"Error: {error_message}")
        popup = Popup(title="Calculation Error", 
                     content=content,
                     size_hint=(0.8, 0.4))
        popup.open()

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
