from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.pickers import MDDatePicker

helpstr='''
ScreenManager:
    WelcomeScreen:
    UsernameScreen:

<WelcomeScreen>
    name: 'welcomescreen'
    MDLabel:
        text: 'Welcome Screen'
        halign : 'center'
        theme_text_color:'Custom'
        text_color: '#fe4987'
        font_style: 'H1'
        font_size: 30
    MDFloatingActionButton:
        icon: 'android'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '60sp'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press:
            root.manager.current='usernamescreen'
            root.manager.transition.direction='left'
    

<UsernameScreen>
    name: 'usernamescreen'
    MDFloatingActionButton:
        icon:'arrow-left'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '45sp'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press:
            root.manager.current='welcomescreen'
            root.manager.transition.direction='right'
        
    MDFloatingActionButton:
        id:disabled_button
        disabled:True
        icon:'arrow-right'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '45sp'
        pos_hint: {'center_x':0.9,'center_y':0.1}
    MDProgressBar:
        value:60
        pos_hint: {'center_y': 0.02}
    MDLabel:
        text: 'Username'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        theme_text_color:'Custom'
        text_color: '#fe4987'
        font_style: 'H1'
        font_size: 30
    MDTextField:
        id:username_text_field
        hint_text: "Enter username"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300

    MDRectangleFlatButton:
        text:'Submit'
        pos_hint:{'center_x':0.5,'center_y':0.35}
        on_press: app.check_username()

        
'''

class WelcomeScreen(Screen):
    pass
class UsernameScreen(Screen):
    pass

sm= ScreenManager()
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(UsernameScreen(name = 'usernamescreen'))

class NewApp(MDApp):
    def build(self):
        self.string = Builder.load_string(helpstr)
        return self.string
    
    def check_username(self):
        self.username_text=self.string.get_screen('usernamescreen'.ids.username_text_field.text)
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.username_text.split()==[]:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title= 'Invalid username',text="Please input a valid username",size_hint=(0.7,0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

        else:
            self.string.get_screen('usernamescreen').ids.disabled_button.disabled: bool = False


    def close_username_dialogue(self,obj):
        self.dialog.dismiss()





NewApp().run()