from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Textbox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDown")


def draw(controls):
    for control in controls:
        control.draw()

# inherite from built-in classes


class Text(str):
    def duplicate(self):
        return self + self
