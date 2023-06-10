from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder 
import filesharer
import time
from kivy.core.clipboard import Clipboard
import webbrowser

Builder.load_file('frontend.kv')

# Create screen classes
class CameraScreen(Screen):
    def start(self):
        """Starts Camera and changes Button text"""
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """Stops camera and changes Button text"""
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    def capture(self):
        """Creates a filename with the current time and captures 
        and saves a photo image under that filename"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f'files/{current_time}.png'
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.img.source = self.filepath




class ImageScreen(Screen):
    link_message = "Create a Link First"
    def create_link(self):
        """Access photo file path, uploads it to web, and inserts the link
        into the label widget."""
        filepath = App.get_running_app().root.ids.camera_screen.filepath
        file_sharer =  filesharer.FileSharer(filepath)
        self.url = file_sharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except: 
            self.ids.link.text = self.link_message

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except: 
            self.ids.link.text = self.link_message




# Make copy of ScreenManager class plus methods we may add.
class RootWidget(ScreenManager):
    pass

# Initialize RootWidget when MainApp (inherits from App) runs
class MainApp(App):
    def build(self):
        return RootWidget()
    
MainApp().run()

