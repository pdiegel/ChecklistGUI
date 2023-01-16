import dearpygui.dearpygui as dpg
from datetime import datetime, date, timedelta


class Timer:
    def __init__(self, pause_tag, display_tag, time_type_tag):
        # time attributes is in seconds
        self.time = "0"
        self.started = False
        self.paused = True  
        self.pause_tag = pause_tag
        self.display_tag = display_tag
        self.time_type = time_type_tag
        self.elapsed_pause = timedelta(0)
    
    def advance_time(self):
        if self.paused:
            return
        # The dearpygui render loop runs at 60 fps
        self.time = datetime.now() - self.start_time - self.elapsed_pause

    
    def reset_timer(self):
        self.time = "0"
        self.started = False
        self.elapsed_pause = timedelta(0)
    
    def resume_timer(self):
        self.paused = False
        self.elapsed_pause += datetime.now() - self.time_paused

    def pause_timer(self):
        self.paused = True
        self.time_paused = datetime.now()
    
    def pause_resume_timer(self, sender):
        if not self.started:
            return

        self.set_button_label(sender)
        if self.paused:
            self.resume_timer()
        else:
            self.pause_timer()

    def display_time(self, sender):
        #hours = self.time.strftime('%H')
        string_time = str(self.time)
        format = 'Seconds'
        if string_time != '0':
            seconds = float(string_time.split(':')[2])
            minutes = float(string_time.split(':')[1]) + (seconds/60)
            hours = float(string_time.split(':')[0]) + (minutes/60)
            output = seconds
            if minutes >= 1:
                if hours >= 1:
                    format = 'Hours'
                    output = hours
                else:
                    format = 'Minutes'
                    output = minutes
        else:
            output = 0
        
        dpg.set_value(sender, format)
        return "{:.2f}".format(output)

    def set_button_label(self, sender):
        if self.paused or self.time == 0:
            label = 'Pause'
        else:
            label = 'Resume'
        dpg.set_item_label(sender, label)
    
    def start_timer(self):
        if not self.started:
            self.started = True
            self.start_time = datetime.now()
            self.paused = False

    def stop_timer(self):
        if not self.started:
            return

        if not self.paused:
            self.pause_timer()
        self.reset_timer()
        self.set_button_label(self.pause_tag)

            
            


    

