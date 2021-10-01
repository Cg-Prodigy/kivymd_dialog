from kivy.core.window import Window
from kivy.factory import Factory
from kaki.app import App
from kivymd.app import MDApp


class DialogClass(App,MDApp):
    CLASSES={
        'EntryPoint':'app_ui.dialog'
    }
    KV_FILES=[
        'app_ui/dialog.kv'
    ]
    AUTORELOADER_PATHS=[
        ('.',{'recursive':True})
    ]
    def build_app(self):
        self.title='Dialog Box'
        Window.size=(360,640)
        return Factory.EntryPoint()


if __name__=='__main__':
    DialogClass().run()