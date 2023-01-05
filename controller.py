

from model import Model
from view import View
import os

class Controller:
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)
        self.file_pass = ""
        self.save_theme = 'Dark Brown1'
        self.dirname = os.path.dirname(__file__)
        self.ini_basename = 'config.ini'



    def main(self,save_theme):
        self.view.main(save_theme)

    def file_load(self,file_pass):
        try:
            self.model.music_load(file_pass)
        except EOFError:
            self.file_readerror_send_view()



        self.file_pass = file_pass
        print('controller')
        print(self.file_pass)

    def play_button_controller(self,loops,start):
        self.model.play_music(loops,start)

    def stop_button_controller(self):
        self.model.stop_music()
    
    def pause_button_controller(self,tgl_pause):
        if  tgl_pause == True:
            self.model.pause_music()
        else:
            self.model.unpause_music()
    def seek_slider_controller(self,loops,start):
        self.model.play_music(loops,start)

    def volume_slider_controller(self,vol_value):
        self.model.set_volume(vol_value)

    def total_second_send_view(self,total_second):
        print("hms_send_view")
        print(total_second)
        self.view.hms_view_update(total_second)

    def file_pass_send_view(self):
        return self.file_pass

    def file_readerror_send_view(self):
        self.view.readerror_popup()

    def ini_file_exists(self):
        if os.path.exists(os.path.join(self.dirname, self.ini_basename)):
            self.save_theme = str(self.model.get_ini_file_theme())
            print(self.save_theme)

        else:
            self.model.set_ini_file()

        

    


if __name__ == '__main__':
    music_player = Controller()
    music_player.ini_file_exists()
    music_player.main(music_player.save_theme)