from abc import ABC, abstractmethod

class Button(ABC):
    '''
    Abstract product class for button
    
    '''
    
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def on_click(self):
        pass

class WindowsButton(Button): 
    '''
    Concrete product classe for Windows button
    
    '''
    def render(self):
        return "Windows Button"
    
    def on_click(self):
        print("Windows Button Clicked")

class HTMLButton(Button):
    '''
    Concrete product classe for HTML button

    '''
    def render(self):
        return "HTML Button"
    
    def on_click(self):
        print("HTML Button Clicked")

class DialogCreator(ABC):
    '''
    Main creator class

    '''
    
    @abstractmethod
    def createButton(self):
        pass
    
    def render(self):
        button = self.createButton()
        button.on_click()
        return button.render()
    
class WindowsDialogCreator(DialogCreator):
    '''
    Concrete creator classe for Windows button

    '''
    
    def createButton(self):
        return WindowsButton()

class HTMLDialogCreator(DialogCreator):
    '''
    Concrete creator classe for HTML button
    
    '''
    
    def createButton(self):
        return HTMLButton()
    
    
if __name__ == "__main__":
    dialog_win = WindowsDialogCreator()
    print(dialog_win.render())
    
    dialog_html = HTMLDialogCreator()
    print(dialog_html.render())