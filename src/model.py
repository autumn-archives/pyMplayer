
import pygame
from pygame import mixer
import audioread.exceptions
import librosa
import configparser
import os



class Model:



    def __init__(self,controller):
        self.controller = controller
        self.sr = 44100
        self.config = configparser.ConfigParser()
        self.dirname = os.path.dirname(__file__)
        self.ini_basename = 'config.ini'
        mixer.init(frequency = self.sr)
    
    def music_load(self,file_pass):
        try:
            mixer.music.load(file_pass)
            self.audio,self.sr = librosa.load(file_pass,self.sr)
            self.total_second = librosa.get_duration(self.audio,self.sr)
            self.controller.total_second_send_view(self.total_second)
        except pygame.error:
            self.controller.file_readerror_send_view()
        except audioread.exceptions.NoBackendError:
            self.controller.file_readerror_send_view()
            


    def play_music(self,loops,start):
        try:
            mixer.music.play(loops,start)
        #ボタンを押してもエラー落ちしないようにこれらのエラーはパスしておく。
        except NameError:
            pass
        except FileNotFoundError:
            pass
        except pygame.error:
            pass

    def stop_music(self):
        mixer.music.stop()

    def pause_music(self):
        mixer.music.pause()
    
    def unpause_music(self):
        mixer.music.unpause()


    def set_volume(self,vol_value):
        mixer.music.set_volume(vol_value)

    def set_ini_file(self,theme='Dark Brown1'):
        self.config['BASE'] = {
        '-theme-': theme
        }
        with open(os.path.join(self.dirname, self.ini_basename), 'w') as file:
            self.config.write(file)

    def get_ini_file_theme(self):
        self.config.read(os.path.join(self.dirname, self.ini_basename))
        return self.config['BASE']['-theme-']


    '''
    def total_second_convert(self,total_second):
        print(total_second)
        self.minuts = total_second // 60
        self.second = total_second % 60
        self.hour = self.minuts // 60
        self.min = self.minuts % 60
        if self.hour == 0:
           self.hms = f"{int(self.min):02}:{int(self.second):02}"
        else:
           self.hms = f"{int(self.hour):02}:{int(self.min):02}:{int(self.second):02}"
        self.controller.hms_send_view(self.total_second,self.hms)
    '''
    