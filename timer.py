import dearpygui.dearpygui as dpg

class Timer:
    def __init__(self, pause_tag, display_tag, time_type_tag):
        # time attributes is in seconds
        self.time = 0
        self.time_minutes = 0
        self.time_hours = 0
        self.started = False
        self.paused = True  
        self.pause_tag = pause_tag
        self.display_tag = display_tag
        self.time_type = time_type_tag
    
    def advance_time(self):
        # The dearpygui render loop runs at 60 fps
        self.time += 1/60
        self.time_minutes = self.time/60
        self.time_hours = self.time_minutes/60
    
    def reset_timer(self):
        self.time = 0
        self.time_minutes = 0
        self.time_hours = 0
        self.started = False
    
    def resume_timer(self):
        self.paused = False

    def pause_timer(self):
        self.paused = True
    
    def pause_resume_timer(self, sender):
        if not self.started:
            return

        self.set_button_label(sender)
        if self.paused:
            self.resume_timer()
        else:
            self.pause_timer()

    def display_time(self, sender):
        if self.time_hours >= 1:
            output = self.time_hours
            format = 'Hours'
        elif self.time_minutes >= 1:
            output = self.time_minutes
            format = 'Minutes'
        else:
            output = self.time
            format = 'Seconds'
        
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
            self.resume_timer()

    def stop_timer(self):
        if not self.started:
            return

        if not self.paused:
            self.pause_timer()
        self.reset_timer()
        self.set_button_label(self.pause_tag)

            
            


    

