from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.metrics import dp

class CalculatorApp(App):
    def build(self):
        # Set default window size for desktop testing
        Window.size = (dp(400), dp(600)) if not App.get_running_app().platform == 'android' else Window.size
        
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        
        # Initialize result label with explicit size handling
        self.result = Label(
            text="", 
            font_size=dp(32), 
            halign="right", 
            valign="middle",
            size_hint=(1, 0.2),
            text_size=(None, None)
        )
        
        layout = BoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        
        # Use non-readonly TextInput with disabled user input
        self.solution = TextInput(
            multiline=False,
            font_size=dp(55),
            halign="right",
            size_hint=(1, 0.2),
            write_tab=False,
            readonly=False,  # Allow programmatic changes
            disabled=True,   # Prevent user typing
            disabled_foreground_color=(1, 1, 1, 1)  # White text when disabled
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
            h_layout = BoxLayout(spacing=dp(10))
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    size_hint=(0.25, 1)
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        
        equals_button = Button(
            text="=", 
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(1, 0.2)
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
            # Prevent multiple operators or leading operators
            if current and self.last_was_operator and button_text in self.operators:
                return
            if current == "" and button_text in self.operators:
                return
            # Prevent multiple decimal points
            if button_text == "." and "." in current:
                return
            new_text = current + button_text
            self.solution.text = new_text
        
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if not text:
            return
        
        # Validate input to prevent unsafe eval
        allowed_chars = set("0123456789.+-*/ ")
        if not all(c in allowed_chars for c in text):
            self.show_error_popup("Invalid characters in expression")
            self.solution.text = ""
            self.result.text = ""
            return
        
        try:
            # Evaluate the expression safely
            solution = str(eval(text, {"__builtins__": {}}, {}))
            self.result.text = solution
            self.solution.text = solution
        except ZeroDivisionError:
            self.show_error_popup("Division by zero")
            self.solution.text = ""
            self.result.text = ""
        except SyntaxError:
            self.show_error_popup("Invalid expression")
            self.solution.text = ""
            self.result.text = ""
        except Exception as e:
            self.show_error_popup(f"Error: {str(e)}")
            self.solution.text = ""
            self.result.text = ""

    def show_error_popup(self, error_message):
        content = Label(text=f"Error: {error_message}", halign="center")
        popup = Popup(
            title="Calculation Error",
            content=content,
            size_hint=(0.8, 0.4),
            auto_dismiss=True
        )
        popup.open()

if __name__ == "__main__":
    CalculatorApp().run()
