from kivy.app import App
from kivy.lang import Builder

class ConvertMetresApp(App):
    def build(self):
        self.title = "Convert Miles"
        self.root = Builder.load_file("from_scratch.kv")
        return self.root

    def handle_convert(self):
            value = self.get_valid_miles() * 1.61
            self.root.ids.output_label.text = "{:.3f}".format(value)

    def handle_increment(self,increment):
        result = self.get_valid_miles() + increment
        self.root.ids.user_input.text = str(result)
        self.handle_convert()

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.user_input.text)
            return value
        except ValueError:
            return 0

ConvertMetresApp().run()