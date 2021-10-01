from kivy.clock import Clock
from kivy.metrics import dp,sp
from kivy.properties import StringProperty,ListProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.selectioncontrol import MDCheckbox

class EntryPoint(MDRelativeLayout):
    dialog=None
    users=['One','Two','Three','Four']
    def __init__(self,**kwargs):
        super(EntryPoint,self).__init__(**kwargs)
    def open_dialog(self):
        if not self.dialog:
            self.dialog=MDDialog(
                title='MDdialog',
                type='simple',
                buttons=[
                    MDFillRoundFlatButton(text='Cancel',on_release=lambda x:self.dialog.dismiss()),
                    MDFillRoundFlatButton(text='Delete',on_release=lambda x:self.dialog.dismiss())
                ],
                items=[
                    DialogItems(text='User One',source='pics/1.jpg'),
                    DialogItems(text='User One',source='pics/2.jpg'),
                    DialogItems(text='User One',source='pics/3.jpg'),
                    DialogItems(text='User One',source='pics/1.jpg')
                ]
        )
        self.dialog.open()
    def close_dialog(self):
        self.dialog.dismiss()


class DialogItems(OneLineAvatarListItem):
    source=StringProperty()
    divider=None