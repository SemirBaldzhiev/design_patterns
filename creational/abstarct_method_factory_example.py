from abc import ABC, abstractmethod

class GUIFactory(ABC):
    '''
    Abstract factory class for GUI
    '''
    
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_checkbox(self):
        pass

class WinFactory(GUIFactory):
    
    def create_button(self):
        return WinButton()
    
    def create_checkbox(self):
        return WinCheckbox()

class MacFactory(GUIFactory):
    
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()

class Button(ABC):
    def render(self):
        pass

class Checkbox(ABC):
    def render(self):
        pass

class WinButton(Button):
    def render(self):
        return "Windows Button"

class MacButton(Button):
    def render(self):
        return "Mac Button"

class WinCheckbox(Checkbox):
    def render(self):
        return "Windows Checkbox"

class MacCheckbox(Checkbox):
    def render(self):
        return "Mac Checkbox"

class Application:
    def __init__(self, factory):
        self.factory = factory
    
    def create_button(self):
        return self.factory.create_button()
    
    def create_checkbox(self):
        return self.factory.create_checkbox()


if __name__ == "__main__":
    os = "win"
    
    if os == "win":
        factory = WinFactory()
    else:
        factory = MacFactory()
    
    app = Application(factory)
    app.create_button().render()
    app.create_checkbox().render()
    
    