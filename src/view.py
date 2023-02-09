

import time
import PySimpleGUI as sg



class View:



    def __init__(self,controller,loops=0,start=0.0,tgl_pause=False,vol_value=1.0):
        self.controller = controller
        self.loops = loops
        self.start = start
        self.loop_flg = False
        self.tgl_pause = tgl_pause
        self.vol_value = vol_value
        self.play_running = False
        self.hms_view_max = 0.0
        self.hms_view_now = 0.0
        self.hms_sl_max = 0.0
        self.seek_sl_val = 0.0
        
        
    def make_window(self,theme='Dark Brown1'):
        if theme:
            sg.theme(theme)
            
        layout = [
            #以下[]で1行の扱いになる。カンマ区切りで横に部品を並べられる
            [sg.Text('ファイル'), sg.InputText(key='-file1-', enable_events=True),
                sg.FileBrowse(key='-file1-',file_types=(('OGG Files', '*.ogg'),))
            ],
            [sg.Slider(range=(0.0,round(self.hms_view_max,1)), default_value=0.0, resolution=0.1, 
                size=(45,20),orientation='h',key='-seek_slider1-',enable_events=True),
                sg.Text(self.convert_hms(self.hms_view_now),key='-now_hms-'),sg.Text(self.convert_hms(self.hms_view_max),key='-max_hms-'),
            ],

            [sg.Button('4' ,key='-play_btn1-',font=('Webdings',10)),
                sg.Button('<' ,key='-stop_btn1-',font=('Webdings',10)),
                sg.Button(';',font=('Webdings',10), key='-pause_btn1-', 
                    enable_events=True, disabled=True),
                sg.Text('X',font=('Webdings',16)),
                sg.Slider(range=(0.0,1.0), default_value=1.0, resolution=0.1, 
                    orientation='h',key='-volume_slider1-',enable_events=True),
                sg.Button('q',key='-loop_Btn1-',font=('Webdings',10)),
                sg.Button('Change Theme',key='-change_theme-'),
                sg.Button('=' ,key='-save_theme-',font=('Wingdings',10))
            ],
            ]
        return sg.Window(title="pyMplayer",layout=layout,finalize=True)


    def close(self):
        self.window.close()


    def file_load(self,values):
        self.file_pass = values['-file1-']
        self.controller.file_load(self.file_pass)
        self.window['-seek_slider1-'].update(range=(0.0,round(self.hms_view_max,1)))


    def push_play(self):
        self.controller.play_button_controller(self.loops,self.start)
        self.play_running = True
        self.tgl_pause = False
        self.pause_tgl_bool(self.tgl_pause)
        self.button_color_change(self.tgl_pause,'-pause_btn1-')
        self.current_time = time.monotonic()

        
    def push_stop(self):
        self.controller.stop_button_controller()
        self.tgl_pause = False
        self.pause_tgl_bool(not self.tgl_pause)
        self.button_color_change(self.tgl_pause,'-pause_btn1-')
        self.hms_view_now= 0.0
        self.start = 0.0
        self.play_running = False
        self.seek_sl_val = 0.0
        self.window['-now_hms-'].update(self.convert_hms(self.hms_view_now))
        self.window['-seek_slider1-'].update(0.0)


    def push_pause(self,values):
        self.tgl_pause = not self.tgl_pause
        self.button_color_change(self.tgl_pause,'-pause_btn1-')
        self.controller.pause_button_controller(self.tgl_pause)
        self.play_running = not self.play_running

        if self.play_running == True:
            self.move_seek_slider(values,'-seek_slider1-')
        

    def pause_tgl_bool(self,tgl_pause):
        self.window['-pause_btn1-'].Update(disabled=tgl_pause)


    def button_color_change(self,btn_bool,whitch_btn):
        button_color_back = sg.theme_button_color()[0]
        button_color = sg.theme_button_color()[1]
        self.window[whitch_btn].update(button_color=f'{button_color} on {button_color_back}' if btn_bool else f'{button_color_back} on {button_color}')


    def move_seek_slider(self,values,slider_name):
        self.start = round(self.hms_view_now,1)
        self.seek_sl_val = values[slider_name]
        self.hms_view_now = values[slider_name]

        if self.play_running == True:
            self.push_play()
            self.play_running = True


    def move_vol_slider(self,values,slider_name):
        self.vol_value = values[slider_name]
        self.controller.volume_slider_controller(self.vol_value)


    def hms_view_update(self,total_second):
        self.hms_view_max = total_second
        self.window['-max_hms-'].update(self.convert_hms(self.hms_view_max))


    def convert_hms(self,total_second,view_dicimal=False):  #00:00:00形式で表示する。1時間以下の場合、時間の桁を表示しない。
        self.minuts = total_second // 60
        self.second = total_second % 60
        self.m_second = (self.second - int(self.second)) * 1000
        self.hour = self.minuts // 60
        self.min = self.minuts % 60

        if self.hour == 0:
           self.hms_cv = f"{int(self.min):02}:{int(self.second):02}"
        else:
           self.hms_cv = f"{int(self.hour):02}:{int(self.min):02}:{int(self.second):02}"

        if view_dicimal == True:    #一応作っておいたが使わないかもしれない。
            self.hms_cv += f":{int(self.m_second)}"
        return self.hms_cv


    def readerror_popup(self):
        sg.popup_ok('ファイルが読み込めませんでした。')


    def save_theme(self):
        send_controller_theme = sg.theme()
        self.controller.save_theme_send_model(send_controller_theme)
        sg.popup('theme_saved!')


    def main(self,save_theme):
        self.window = self.make_window(save_theme)

        while True:
            # ウィンドウ表示
            event, values = self.window.read(timeout=100)
        
            #クローズボタンの処理
            if event == sg.WINDOW_CLOSED:
                print('exit')
                break

            elif event == "-file1-":
                self.file_load(values)
                
            elif event == '-play_btn1-':
                self.push_play()

            elif event == '-stop_btn1-':
                self.push_stop()
            
            elif event == '-pause_btn1-':
                self.push_pause(values)
            elif event == '-volume_slider1-':
                self.move_vol_slider(values,'-volume_slider1-')
                
            elif event == '-seek_slider1-':
                self.move_seek_slider(values,'-seek_slider1-')

            elif event == '-loop_Btn1-':    #ループ用ボタンのイベント。-1の時ループする。0はしない。
                self.loop_flg = not self.loop_flg
                self.loops = -1 if self.loop_flg else 0
                self.button_color_change(self.loop_flg,'-loop_Btn1-')
                self.move_seek_slider(values,'-seek_slider1-')

            elif event == '-change_theme-':
                event, values = sg.Window('Choose Theme', [[sg.Combo(sg.theme_list(), readonly=True, key='-theme_list-'), sg.OK(), sg.Cancel()]]).read(close=True)

                if event == 'OK':
                    self.push_stop()
                    self.play_running = False
                    self.window.close()
                    self.window = self.make_window(values['-theme_list-'])
                    self.window['-file1-'].update(self.controller.file_path_send_view())


            elif event == '-save_theme-':
                self.save_theme()

            if self.play_running == True:   #再生中のシークバー制御
                self.hms_view_now = time.monotonic() - self.current_time + self.seek_sl_val
                self.window['-now_hms-'].update(self.convert_hms(self.hms_view_now))
                self.window['-seek_slider1-'].update(self.hms_view_now)

                if self.hms_view_now >= self.hms_view_max:

                    if self.loop_flg == False:
                        self.play_running = False   #ループフラグが無いときはシークバーを止める。
                    else:
                        self.hms_view_now = 0.0
                        self.start = 0.0
                        self.seek_sl_val = 0.0
                        self.current_time = time.monotonic()
                        self.window['-seek_slider1-'].update(self.hms_view_now)
                        
                        
        View.close(self)
        

